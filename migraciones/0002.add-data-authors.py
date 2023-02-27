from yoyo import step
__depends__ = {'0001.create-authors'}
steps = [
   step(
       "insert into authors(first_name, last_name) values('nombre1','ape1'); insert into authors(first_name, last_name) values('nombre2','ape2');  insert into authors(first_name, last_name) values('nombre3','ape3'); insert into authors(first_name, last_name) values('nombre4','ape4');", 
       "DROP TABLE authors",
       
   )
]

