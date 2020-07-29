import conex
import models.user



# from orator import DatabaseManager
# from orator import Model


# select
# results = conex.connec().select('select * from users where id = 1')
# print(results)

# user=conex.connec().table('users').first()
# print(user)

# users=conex.connec().table('users').get()
# for user in users:
#     print(user['nombre'])

# user=conex.connec().table('users').where('nombre','Carla Rmirez').first()
# print(user['correo'])

# users=conex.connec().table('users').where_in('id',[1,2]).get()
# for user in users:
#     print(user['nombre'])

# users=conex.connec().table('users').where_not_in('id',[1,2]).get()
# for user in users:
#     print(user['nombre'])

# query=conex.connec().table('users').order_by('nombre','asc').get()
# for name in query:
#     print(name['nombre'])

# records=conex.connec().table('users').left_join('tipodocumento','users.tipo_documento_id','=','tipodocumento.id').get()
# for record in records:
#     print(record)

# update
# conex.connec().table('users').where('id', 1).update(nombre='Carlos Samalvides')

# insert
#conex.connec().table('users').insert(nombre='Braulio Berlanga', correo='braber_20@gmail.com',tipo_documento_id=3,documento='923729',estado_user_id=2)

# delete
# conex.connec().table('users').where('documento', '=','923729').delete()

# ORM

conex.connec()
user = models.user.User.find(1)
print(user.nombre)
