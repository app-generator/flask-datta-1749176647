# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Clientes(db.Model):

    __tablename__ = 'Clientes'

    id = db.Column(db.Integer, primary_key=True)

    #__Clientes_FIELDS__
    codigo = db.Column(db.String(255),  nullable=True)
    nombre = db.Column(db.Text, nullable=True)
    direccion = db.Column(db.Text, nullable=True)
    telefono = db.Column(db.Text, nullable=True)
    saldo = db.Column(db.Integer, nullable=True)

    #__Clientes_FIELDS__END

    def __init__(self, **kwargs):
        super(Clientes, self).__init__(**kwargs)


class Proveedores(db.Model):

    __tablename__ = 'Proveedores'

    id = db.Column(db.Integer, primary_key=True)

    #__Proveedores_FIELDS__
    codigo = db.Column(db.String(255),  nullable=True)
    nombre = db.Column(db.Text, nullable=True)
    direccion = db.Column(db.Text, nullable=True)
    telefono = db.Column(db.Text, nullable=True)
    saldo = db.Column(db.Integer, nullable=True)

    #__Proveedores_FIELDS__END

    def __init__(self, **kwargs):
        super(Proveedores, self).__init__(**kwargs)


class Pagos(db.Model):

    __tablename__ = 'Pagos'

    id = db.Column(db.Integer, primary_key=True)

    #__Pagos_FIELDS__
    banco = db.Column(db.String(255),  nullable=True)
    cod_proveedor = db.Column(db.String(255),  nullable=True)
    monto = db.Column(db.Integer, nullable=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Pagos_FIELDS__END

    def __init__(self, **kwargs):
        super(Pagos, self).__init__(**kwargs)


class Recibos(db.Model):

    __tablename__ = 'Recibos'

    id = db.Column(db.Integer, primary_key=True)

    #__Recibos_FIELDS__
    banco = db.Column(db.String(255),  nullable=True)
    cod_cliente = db.Column(db.String(255),  nullable=True)
    monto = db.Column(db.Integer, nullable=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Recibos_FIELDS__END

    def __init__(self, **kwargs):
        super(Recibos, self).__init__(**kwargs)


class Bancos(db.Model):

    __tablename__ = 'Bancos'

    id = db.Column(db.Integer, primary_key=True)

    #__Bancos_FIELDS__
    nombre = db.Column(db.Text, nullable=True)
    saldo = db.Column(db.Integer, nullable=True)

    #__Bancos_FIELDS__END

    def __init__(self, **kwargs):
        super(Bancos, self).__init__(**kwargs)


class Inventario(db.Model):

    __tablename__ = 'Inventario'

    id = db.Column(db.Integer, primary_key=True)

    #__Inventario_FIELDS__
    cod_suc = db.Column(db.String(255),  nullable=True)
    nombre = db.Column(db.Integer, nullable=True)
    saldo = db.Column(db.Integer, nullable=True)

    #__Inventario_FIELDS__END

    def __init__(self, **kwargs):
        super(Inventario, self).__init__(**kwargs)


class Ingresos(db.Model):

    __tablename__ = 'Ingresos'

    id = db.Column(db.Integer, primary_key=True)

    #__Ingresos_FIELDS__
    concepto = db.Column(db.Text, nullable=True)
    referencia = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    monto = db.Column(db.Integer, nullable=True)
    cliente = db.Column(db.String(255),  nullable=True)
    costo_venta = db.Column(db.Integer, nullable=True)
    banco_ad1 = db.Column(db.Integer, nullable=True)
    banco_ad2 = db.Column(db.Integer, nullable=True)
    banco_ad3 = db.Column(db.Integer, nullable=True)
    banco_ad4 = db.Column(db.Integer, nullable=True)
    banco_ad5 = db.Column(db.Integer, nullable=True)
    banco1 = db.Column(db.String(255),  nullable=True)
    banco2 = db.Column(db.String(255),  nullable=True)
    banco3 = db.Column(db.String(255),  nullable=True)
    banco4 = db.Column(db.String(255),  nullable=True)
    banco5 = db.Column(db.String(255),  nullable=True)
    forma_pago = db.Column(db.String(255),  nullable=True)

    #__Ingresos_FIELDS__END

    def __init__(self, **kwargs):
        super(Ingresos, self).__init__(**kwargs)


class Egresos(db.Model):

    __tablename__ = 'Egresos'

    id = db.Column(db.Integer, primary_key=True)

    #__Egresos_FIELDS__
    tipo_egreso = db.Column(db.Text, nullable=True)
    concepto = db.Column(db.Text, nullable=True)
    referencia = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    monto = db.Column(db.Integer, nullable=True)
    banco = db.Column(db.String(255),  nullable=True)
    forma_pago = db.Column(db.String(255),  nullable=True)

    #__Egresos_FIELDS__END

    def __init__(self, **kwargs):
        super(Egresos, self).__init__(**kwargs)


class Sucursal(db.Model):

    __tablename__ = 'Sucursal'

    id = db.Column(db.Integer, primary_key=True)

    #__Sucursal_FIELDS__
    cod_suc = db.Column(db.String(255),  nullable=True)
    nombre = db.Column(db.Text, nullable=True)

    #__Sucursal_FIELDS__END

    def __init__(self, **kwargs):
        super(Sucursal, self).__init__(**kwargs)



#__MODELS__END
