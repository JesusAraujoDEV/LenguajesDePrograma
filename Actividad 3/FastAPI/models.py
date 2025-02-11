from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel

class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    age: int = Field(default=None)
    email: EmailStr = Field(default=None)

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class Transaction(BaseModel):
    id: int
    amount: int
    description: str
    #date: str
    #customer_id: int

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def ammount_total(self):
        return sum([t.amount for t in self.transactions])
    
    # Asignar total automáticamente a ammount_total
    def __init__(self, **data):
        super().__init__(**data)
        self.total = self.ammount_total