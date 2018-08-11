CREATE TABLE customers (
    id serial primary key,
    name varchar(128) unique not null,

    created_at timestamp without time zone,
    updated_at timestamp without time zone
);
ALTER TABLE customers OWNER TO postgres;

INSERT INTO customers(name, created_at, updated_at) VALUES
    ('Milan', NOW(), NOW()),
    ('Elena', NOW(), NOW()),
    ('Sarah', NOW(), NOW());


CREATE TABLE pizza (
    id serial primary key,
    name varchar(128) unique not null,
    description text,

    created_at timestamp without time zone,
    updated_at timestamp without time zone
);
ALTER TABLE pizza OWNER TO postgres;

INSERT INTO pizza(name, description, created_at, updated_at) VALUES
    ('Pepperoni', 'Pepperoni (also known as pepperoni sausage) is an American variety of salami, made from cured pork and beef mixed together and seasoned with paprika or other chili pepper.', NOW(), NOW()),
    ('Margherita', 'Pizza Margherita is a typical Neapolitan pizza, made with San Marzano tomatoes, mozzarella fior di latte,[1] fresh basil, salt and extra-virgin olive oil.', NOW(), NOW()),
    ('Capricciosa', 'Pizza capricciosa is a style of pizza in Italian cuisine prepared with mozzarella cheese, Italian baked ham, mushroom, artichoke and tomato.', NOW(), NOW());


CREATE TYPE pizza_size AS ENUM (
    '30cm',
    '50cm'
);

CREATE TABLE orders (
    id serial primary key,
    pizza_id int not null references pizza (id),
    pizza_size pizza_size not null,
    customer_id int not null references customers (id),
    customer_name varchar(128) not null,
    customer_address varchar(256) not null,

    created_at timestamp without time zone,
    updated_at timestamp without time zone
);
ALTER TABLE orders OWNER TO postgres;

INSERT INTO orders(pizza_id, pizza_size, customer_id, customer_name, customer_address, created_at, updated_at) VALUES
    (1, '50cm', '1', 'Milan', 'Berlinstr 1, Berlin 10101', NOW(), NOW()),
    (2, '50cm', '2', 'Elena', 'Berlinstr 1, Berlin 10101', NOW(), NOW()),
    (3, '50cm', '3', 'Sarah', 'Moscowstr 5, Berlin 10201', NOW(), NOW());
