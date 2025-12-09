CREATE DATABASE turnero_estrella
USE turnero_estrella;
CREATE table hospitales(
	Id_table int auto_increment primary key,
	nombre VARCHAR(20),
	especialidad VARCHAR(50),
    horario TIME,
    direccion varchar(50)
    );
    
CREATE table doctores (
id int auto_increment primary key,
nombre varchar(30),
consultorio int (30),
especialidad varchar(50)
 );


CREATE table horarios (
id_horarios int auto_increment primary key,
dia_semana varchar(10) NOT NULL,
hora_inicio TIME NOT NULL,
hora_fin TIME NOT NULL
);


CREATE table pacientes (
id int auto_increment primary key,
nombre varchar(20),
apellido varchar(20),
fecha_nacimiento DATE NOT NULL,
contraseña varchar(10),
telefono varchar(15),
email varchar(50),
seguro_medico varchar(50)
);

INSERT INTO doctores (nombre, consultorio, especialidad) values ('Maria', 7, 'pedriatría');
INSERT INTO doctores (nombre, consultorio, especialidad) values ('Juan', 7, 'Ortodoncia');

INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, contraseña, telefono , email, seguro_medico) values ( 'Valentina', 'Rosarios', '2009-11-20', 'aceituna', '351222029', 'Vale@gimail.com', 'Blue Cross');
INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, contraseña, telefono , email, seguro_medico) values ('Carlos,','Suarez', '2001-09-05', 'mer3ngue' '351867500', 'Carlos@gimail.com', 'Blue Cross');

INSERT INTO hospitales (nombre, especialidad, horario, direccion) values ( 'Hospital General','Cardiologia', '09:00:00' ,'Av Libertador' );
INSERT INTO hospitales (nombre, especialidad, horario, direccion) values ('Hosoital Infantil','Odontoligía', '08:00:00', 'Luis de Góngora');

INSERT INTO horarios (dia_semana, hora_inicio, hora_fin) values ( 'Lunes','08:00:00', '12:00:00');
INSERT INTO horarios (dia_semana, hora_inicio, hora_fin) values ('Jueves' ,'06:00:00', '13:00:00');
 
 SELECT nombre, apellido
 FROM pacientes
 WHERE telefono='351867500';
 
 UPDATE doctores
 SET consultorio= 8
 WHERE especialidad='Ortodoncia';
 
 DELETE from pacientes
 WHERE apellido = 'Suarez';
 
 select *
 from horarios;