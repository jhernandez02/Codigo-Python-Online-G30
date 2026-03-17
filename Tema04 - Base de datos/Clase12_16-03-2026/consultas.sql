# Listamos todas las citas y mostramos los nombres de doctores y pacientes
SELECT c.id, doctor_id, d.nombre As doctores, paciente_id, p.nombre AS pacientes, fecha_cita
FROM citas c
INNER JOIN doctores d ON d.id=c.doctor_id
INNER JOIN pacientes p ON p.id=c.paciente_id;

# Listamos todas las citas de un doctor en especifico
SELECT c.id, doctor_id, d.nombre As doctores, paciente_id, p.nombre AS pacientes, fecha_cita
FROM citas c
INNER JOIN doctores d ON d.id=c.doctor_id
INNER JOIN pacientes p ON p.id=c.paciente_id
INNER JOIN especialidades e ON e.id=
WHERE doctor_id=2;

# Listamos todas las citas de un doctor y un paciente en especifico
SELECT c.id, doctor_id, d.nombre As doctores, paciente_id, p.nombre AS pacientes, fecha_cita
FROM citas c
INNER JOIN doctores d ON d.id=c.doctor_id
INNER JOIN pacientes p ON p.id=c.paciente_id
WHERE doctor_id=2 AND paciente_id=3;

# Listamos todas las citas de un doctor, pacientes y especialidad de doctor
SELECT c.id, doctor_id, d.nombre As doctores, paciente_id, p.nombre AS pacientes, fecha_cita
FROM citas c
INNER JOIN doctores d ON d.id=c.doctor_id
INNER JOIN pacientes p ON p.id=c.paciente_id
WHERE doctor_id=2 AND paciente_id=3;

# Actualizar el campo especialidad por especialidad_id,
# Convertir el campos a int4, en la tabla doctores

# Listamos todas las citas y los datos de los doctores, pacientes y especialidades
SELECT c.id, doctor_id, d.nombre AS doctores, e.nombre AS especialidad, paciente_id, p.nombre AS pacientes, fecha_cita
FROM citas c
INNER JOIN doctores d ON d.id=c.doctor_id
INNER JOIN pacientes p ON p.id=c.paciente_id
INNER JOIN especialidades e ON e.id=d.especialidad_id;

# Listamos todas las citas y los datos de los doctores, pacientes y especialidades y fecha creación
SELECT c.id, doctor_id, 
    d.nombre AS doctores, 
    e.nombre AS especialidad, 
    paciente_id, 
    p.nombre AS pacientes, 
    TO_CHAR(c.fecha_cita,'DD/MM/YYYY HH:mi:ss') AS fecha_cita,
    TO_CHAR(c.fecha_registro AT TIME ZONE '-5','DD/MM/YYYY HH:mi:ss') AS fecha_registro
FROM citas c
INNER JOIN doctores d ON d.id=c.doctor_id
INNER JOIN pacientes p ON p.id=c.paciente_id
INNER JOIN especialidades e ON e.id=d.especialidad_id;