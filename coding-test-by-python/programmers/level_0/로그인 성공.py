# def solution(id_pw, db):
#     input_id = id_pw[0]
#     input_pw = id_pw[1]
#
#     return login(input_id, input_pw, db)


# def login(input_id, input_pw, db):
#
#     for account in db:
#         db_account_id = account[0]
#         db_account_pw = account[1]
#         if input_id == db_account_id:
#             return 'login' if input_pw == db_account_pw else 'wrong pw'
#     return 'fail'


def solution(id_pw, db):

    input_id = id_pw[0]
    input_pw = id_pw[1]

    dict_db = dict(db)
    find_pw = dict_db.get(input_id)

    if db_pw := find_pw:
        return "login" if db_pw == input_pw else "wrong pw"

    return "fail"


# print(f'결과 = {solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])}')
# print(f'결과 = {solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]])}')
print(f'결과 = {solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]])}')
