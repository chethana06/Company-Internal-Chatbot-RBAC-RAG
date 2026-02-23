from database import SessionLocal, engine, Base
from models import User
from auth import hash_password


def seed_users():
    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    users = [
        User(username="hr_user", hashed_password=hash_password("hr123"), role="HR"),
        User(username="finance_user", hashed_password=hash_password("fin123"), role="Finance"),
        User(username="ceo", hashed_password=hash_password("ceo123"), role="C-Level"),
        User(username="eng_user", hashed_password=hash_password("eng123"), role="Engineering"),
        User(username="marketing_user", hashed_password=hash_password("mark123"), role="Marketing"),
        User(username="employee_user", hashed_password=hash_password("emp123"), role="Employee"),
    ]

    db.add_all(users)
    db.commit()
    db.close()

    print("✅ Users inserted successfully")


if __name__ == "__main__":
    seed_users()
