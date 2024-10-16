
CREATE TABLE  if NOT EXISTS Recipes(
    id SERIAL  PRIMARY KEY,
    type varchar(32) NOT NULL,
    name varchar(64) NOT NULL,
    ingredients varchar NOT NULL,
    instructions varchar NOT NULL
);

INSERT INTO Recipes (type, name, ingredients, instructions)
VALUES
    ('Main Course', 'Grilled Chicken', 'Chicken breast, Olive oil, Salt, Pepper', 'Grill chicken breast for 5-7 minutes per side.'),
    ('Appetizer', 'Bruschetta', 'Bread, Tomatoes, Basil, Mozzarella', 'Toast bread, top with tomatoes, basil, and mozzarella.'),
    ('Side Dish', 'Roasted Vegetables', 'Carrots, Broccoli, Olive oil, Salt, Pepper', 'Toss vegetables with olive oil, salt, and pepper. Roast at 400°F for 20-25 minutes.');