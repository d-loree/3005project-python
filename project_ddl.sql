CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role VARCHAR(7) CHECK (role IN ('member', 'user', 'admin'))
);

CREATE TABLE trainers (
    trainer_id INT PRIMARY KEY REFERENCES users(id)
);

CREATE TABLE admins (
    admin_id INT PRIMARY KEY REFERENCES users(id)
);

CREATE TABLE members (
    member_id INT PRIMARY KEY REFERENCES users(id),
    goal_weight NUMERIC(5, 2) NOT NULL,
    goal_deadline DATE NOT NULL,
    height NUMERIC(5, 2) NOT NULL,
    weight NUMERIC(5, 2) NOT NULL
);

CREATE TABLE trainer_availability (
    availability_id SERIAL PRIMARY KEY,
    trainer_id INT REFERENCES trainers(trainer_id),
    day_of_the_week VARCHAR(9) NOT NULL CHECK (day_of_the_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE group_sessions (
    group_session_id SERIAL PRIMARY KEY,
    session_name TEXT NOT NULL,
    trainer_id INT REFERENCES trainers(trainer_id),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE training_sessions (
    session_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(member_id),
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE group_session_registrations (
    member_id INT REFERENCES members(member_id),
    group_session_id INT REFERENCES group_sessions(group_session_id),
    PRIMARY KEY (member_id, group_session_id)
);

CREATE TABLE individual_training_sessions_registrations (
    session_id INT REFERENCES training_sessions(session_id),
    member_id INT REFERENCES members(member_id),
    PRIMARY KEY (session_id, member_id)
);

CREATE TABLE room_bookings (
    room_booking_id SERIAL PRIMARY KEY,
    room_id INT NOT NULL,
    trainer_id INT REFERENCES trainers(trainer_id),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE fitness_equipment (
    equipment_id SERIAL PRIMARY KEY,
    needs_maintenance BOOLEAN NOT NULL,
    last_maintenance DATE NOT NULL
);
