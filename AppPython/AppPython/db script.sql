-- Active: 1698756320233@@127.0.0.1@3306@test
create table tbl_categorias(
    cod_categoria int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) not null
);
create table tbl_productos (
    cod_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) not null,
    descripcion varchar(200),
    valor_unitario int not NULL,
    stock int not null,
    cod_categoria int,
    constraint fk_categoria FOREIGN KEY (cod_categoria) 
    REFERENCES tbl_categorias (cod_categoria) ON DELETE CASCADE ON UPDATE CASCADE 
);