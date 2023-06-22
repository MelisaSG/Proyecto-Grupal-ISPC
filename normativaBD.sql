
DROP DATABASE IF EXISTS normativasispc;

create database normativasispc;

USE normativasispc;

DROP TABLE IF exists tipos;

CREATE TABLE tipos (id_tipo INT not null, 
			nombre VARCHAR(20) not null,
            PRIMARY KEY(id_tipo));	
            
INSERT INTO tipos (id_tipo, nombre) VALUES (1,"LEY");    
INSERT INTO tipos (id_tipo, nombre) VALUES (2,"DECRETO");            
INSERT INTO tipos (id_tipo, nombre) VALUES (3,"RESOLUCIÓN");       

select * from tipos;             

DROP TABLE IF exists categorias;

CREATE TABLE categorias (id_categoria INT not null, 
			nombre VARCHAR(20) not null,
            PRIMARY KEY(id_categoria));	
            
INSERT INTO categorias (id_categoria, nombre) VALUES (1,"LABORAL");    
INSERT INTO categorias (id_categoria, nombre) VALUES (2,"PENAL");            
INSERT INTO categorias (id_categoria, nombre) VALUES (3,"CIVIL");  
INSERT INTO categorias (id_categoria, nombre) VALUES (4,"COMERCIAL");    
INSERT INTO categorias (id_categoria, nombre) VALUES (5,"FAMILIA Y SUCESIONES");            
INSERT INTO categorias (id_categoria, nombre) VALUES (6,"AGRARIO Y AMBIENTAL");      
INSERT INTO categorias (id_categoria, nombre) VALUES (7,"MINERO"); 
INSERT INTO categorias (id_categoria, nombre) VALUES (8,"DERECHO INFORMATICO"); 

select * from categorias;             

DROP TABLE IF exists jurisdicciones;

CREATE TABLE jurisdicciones (id_jurisdiccion INT not null, 
			nombre VARCHAR(20) not null,
            organo_legislativo VARCHAR(50) not null,
            PRIMARY KEY(id_jurisdiccion));	
            
INSERT INTO jurisdicciones (id_jurisdiccion, nombre, organo_legislativo) VALUES (1,"NACIONAL", "CONGRESO NACIONAL");    
INSERT INTO jurisdicciones (id_jurisdiccion, nombre, organo_legislativo) VALUES (2,"PROVINCIAL", "LEGISLATURA PROVINCIAL");            

select * from jurisdicciones;             


DROP TABLE IF exists leyes;

CREATE TABLE leyes (id_leyes INT not null, 
			numero_registro VARCHAR(20) not null,
            nombre VARCHAR(50) not null,
            categoria INT,
            numero_normativa VARCHAR(50),
            fecha DATE,
            jurisdiccion INT,
            tipo_normativa INT,
            descripcion VARCHAR(200),
            palabra_clave VARCHAR(100),
            PRIMARY KEY(id_leyes));	
            
INSERT INTO leyes (id_leyes, numero_registro, nombre, categoria, numero_normativa, fecha, jurisdiccion, tipo_normativa, descripcion,palabra_clave
)                         VALUES (1,"1",  "Ley de Contrato de Trabajo", 1,  '20.744', '2021-01-01', 1, 1,'Contrato, Trabajo','Contrato, Trabajo' );    
INSERT INTO leyes (id_leyes, numero_registro, nombre, categoria, numero_normativa, fecha, jurisdiccion, tipo_normativa, descripcion,palabra_clave
)                         VALUES (2,"2",  "Ley de Teletrabajo", 1,  '27.555', '2022-02-01', 1, 1,'Teletrabajo','Teletrabajo' );   
INSERT INTO leyes (id_leyes, numero_registro, nombre, categoria, numero_normativa, fecha, jurisdiccion, tipo_normativa, descripcion,palabra_clave
)                         VALUES (3,"3",  "Ley de Ejercicio Prof.de la Informática en Cba.", 8,  '7642', '2023-03-01', 2, 1,'Informática, Ejercicio Profesional','Informática, Ejercicio Profesional' );   
select * from leyes;  