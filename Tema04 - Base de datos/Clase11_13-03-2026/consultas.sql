# Eliminamos las tablas, primero las que llevan referencias.
DROP TABLE citas;
DROP TABLE pacientes;
DROP TABLE doctores;

# Limpiamos todo los registros de la tabla citas
TRUNCATE TABLE citas;

# Insertar registros en la tabla pacientes
INSERT INTO pacientes (nombre,correo,telefono) VALUES 
('Ana Gomez', 'ana.gomez@mail.com','555-1234'),
('Luis Ramirez', 'luis.ramirez@mail.com','555-4567'),
('Karen Mendoza', 'karen.mendoza@mail.com','333-1234');

# Insertar registros en la tabla doctores
INSERT INTO doctores (nombre,especialidad) VALUES 
('Dra Carmen Lopez', 'Cardiología'),
('Dr Juan Morales', 'Endocrinología'),
('Dra Silvia Gonzales', 'Medicina General');

# Insertar registros en la tabla citas
INSERT INTO citas (paciente_id, doctor_id, fecha_cita, estado) VALUES 
(1, 3, '2026-03-30', 'P'),
(2, 1, '2026-03-31', 'P'),
(3, 2, '2026-03-30', 'P'),
(1, 2, '2026-03-31', 'P'),
(3, 2, '2026-03-31', 'P');

# Seleccionamos todos los campos y registros de la tabla citas
SELECT * FROM citas;

# Selecionamos los campos id y nombre de todos los registro de la tabal citas
SELECT id, nombre FROM pacientes;

# Ingresamos un nuevo registro en la tabla doctores
INSERT INTO doctores (nombre, especialidad) VALUES ('Dr Oscar Roman', 'Medicina General');

# Seleccionamos todos los doctores con la especialidad de "Medicina General"
SELECT * FROM doctores WHERE especialidad='Medicina General';

# Seleccionamos todos los doctores que no pertenecen a la especialidad de "Medicina General"
SELECT * FROM doctores WHERE especialidad<>'Medicina General';

# Actualizamos la fecha de la cita en el registro del paciente con id 3 con el doctor 
UPDATE citas SET fecha_cita='2026-04-30' 
WHERE paciente_id=3 AND doctor_id=2 AND fecha_cita='2026-03-31';

# Seleccionamos todos los doctores cuyo nombre empieza con "Dr"
SELECT * FROM doctores WHERE nombre LIKE 'Dr%';

# Actualizamos el campo especialidad de la tabla es docteres cuyo id es 2
UPDATE doctores SET especialidad='Endocrinología' WHERE id=2;

# Seleccionamos todos los doctores cuya especialidad termina en "ía"
SELECT * FROM doctores WHERE especialidad LIKE '%ía';

# Contar la cantidad de pacientes que hay
SELECT COUNT(id) FROM pacientes;

# Seleccionamos las citas solo de marzo
SELECT * FROM citas WHERE fecha_cita BETWEEN '2026-03-01' AND '2026-03-31';
SELECT * FROM citas WHERE fecha_cita::text LIKE '2026-03%';
SELECT * FROM citas WHERE fecha_cita>='2026-03-01' AND fecha_cita <='2026-03-31';

# Contamos todas las citas de marzo
SELECT COUNT(*) FROM citas WHERE fecha_cita BETWEEN '2026-03-01' AND '2026-03-31';

# Formateamos la fecha de las citas
SELECT doctor_id, paciente_id, to_char(fecha_cita, 'DD/MM/YYYY'), estado FROM citas;

