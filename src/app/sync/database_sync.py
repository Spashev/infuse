from sqlalchemy.orm import Session
from sqlalchemy.orm import make_transient

from app.database.models import Category, Company, Document, Image, CategoryCompany


def sync_data(dev_session: Session, prod_session: Session):
    sync_table_data(dev_session, prod_session, Category)
    sync_table_data(dev_session, prod_session, Company)
    sync_table_data(dev_session, prod_session, Document)
    sync_table_data(dev_session, prod_session, Image)
    sync_table_data(dev_session, prod_session, CategoryCompany)


def sync_table_data(dev_session, prod_session, model):
    dev_data = dev_session.query(model).all()
    prod_data = prod_session.query(model).all()

    dev_data_dict = {item.id: item for item in dev_data}
    prod_data_dict = {item.id: item for item in prod_data}

    for dev_id, dev_item in dev_data_dict.items():
        if dev_id not in prod_data_dict:
            dev_session.expunge(dev_item)
            make_transient(dev_item)
            prod_session.add(dev_item)
        else:
            prod_item = prod_data_dict[dev_id]
            if isinstance(dev_item, Category):
                prod_item.title = dev_item.title
                prod_item.description = dev_item.description
            elif isinstance(dev_item, Company):
                prod_item.site_url = dev_item.site_url
                prod_item.title = dev_item.title
                prod_item.description = dev_item.description
            elif isinstance(dev_item, Document):
                prod_item.title = dev_item.title
                prod_item.description = dev_item.description
                prod_item.company_id = dev_item.company_id
            elif isinstance(dev_item, Image):
                prod_item.image_url = dev_item.image_url
                prod_item.document_id = dev_item.document_id

    for prod_id, prod_item in prod_data_dict.items():
        if prod_id not in dev_data_dict:
            prod_session.delete(prod_item)

    prod_session.commit()
