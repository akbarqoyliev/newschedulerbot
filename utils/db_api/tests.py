from utils.db_api.sqlite import Database


def test():
    db = Database(path_to_db='test.db')
    db.create_table_users()
    db.add_user(1, "One", "email", 'UTC+5', '{"dars":"wedwe","tala":"ferwf"}', 'uz')
    db.add_user(2, "olim", "olim@gmail.com", 'uz')
    db.add_user(3, 1, 1)
    db.add_user(4, 1, 1)
    db.add_user(5, "John", "john@mail.com")

    users = db.select_all_users()
    print(f"Barcha fodyalanuvchilar: {users}")

    user = db.select_user(id=5)
    print(f"Bitta foydalanuvchini ko'rish: {user}")

    db.update_language('ru','5')
    db.update_schedule_dict('{"sccdsa":"wDAf"}','2')
    db.update_timezone('UTC+3',3)
    # print(db.select_user())

def test_schedules():
    ds = Database(path_to_db='test2.db')
    ds.create_tables_weekdays()
    ds.add_schedule(243,'sfv',True,'12:08','adabiyot,math')
    ds.add_schedule(4134,'cwer34')
    ds.add_schedule(413,'cerf')
    print(ds.count_schedule())
    ds.update_situation('sunday',True,'cerf')
    ds.update_warning_time('monday','22:09','cerf')
    ds.update_text('monday',"math,jt,kimyo",'cwer34')
    day = ds.select_schedule('monday',table_id='sfv',user_id=243)
    print(day)

# test()
# test_schedules()