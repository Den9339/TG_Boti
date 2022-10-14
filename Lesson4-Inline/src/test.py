from loader import db

# print(db.select_all_users())
# print(db.select_user_info(id=341778320))
# print(db.update_user_phone(id=341778320, phone='1234567'))
# print(db.select_user_info(id=341778320))
# print(db.delete_user(id=341778320))
# print(db.select_all_users())

# print(db.select_all_items())
# print(db.select_item(id=341778320))
# print(db.update_items_info(id=341778320, name='Кабачоhsydjtfк', quantity=1))
# print(db.select_item(id=341778320))
# # print(db.delete_item(id=341778320))
# print(db.select_all_items())

db.add_item(id=1, name='Помидоры', quantity=30, photo_path='src\db_api\database\prducy_photo\tomat.jpg')
db.add_item(id=2, name='Огурцы', quantity=20, photo_path='src\db_api\database\prducy_photo\orurec.jpg')
db.add_item(id=3, name='Тыква', quantity=46, photo_path='src\db_api\database\prducy_photo\tikva.jpg')
db.add_item(id=4, name='Кабачок', quantity=15, photo_path='src\db_api\database\prducy_photo\Kabachok.jpg')
print(db.select_all_items())
print(db.get_items_count())

