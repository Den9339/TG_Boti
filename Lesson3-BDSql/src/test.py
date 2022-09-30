from loader import db

# print(db.select_all_users())
# print(db.select_user_info(id=341778320))
# print(db.update_user_phone(id=341778320, phone='1234567'))
# print(db.select_user_info(id=341778320))
# print(db.delete_user(id=341778320))
# print(db.select_all_users())

print(db.select_all_items())
print(db.select_item(id=341778320))
print(db.update_items_info(id=341778320, name='Кабачок', quantity=1))
print(db.select_item(id=341778320))
# print(db.delete_item(id=341778320))
print(db.select_all_items())