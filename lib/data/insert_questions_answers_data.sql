-- add questions in the Questions Table in the quiz_sphere.db

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(1, 'World History', 'Who was the first emperor of China?', 1),
(2, 'World History', 'What year did the Berlin Wall fall?', 1),
(3, 'World History', 'Which country gifted the Statue of Liberty to the USA?', 1),
(4, 'World History', 'What was the main cause of World War I?', 1),
(5, 'World History', 'Who discovered America?', 1);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(6, 'Science Discoveries', 'What does DNA stand for?', 2),
(7, 'Science Discoveries', 'Who developed the theory of relativity?', 2),
(8, 'Science Discoveries', 'What is the chemical symbol for gold?', 2),
(9, 'Science Discoveries', 'Who invented the telephone?', 2),
(10, 'Science Discoveries', 'What year was Pluto reclassified as a dwarf planet?', 2);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(11, 'Literature', 'Who wrote "1984"?', 3),
(12, 'Literature', 'What is the main theme of "The Great Gatsby"?', 3),
(13, 'Literature', 'Which play by Shakespeare includes the character Puck?', 3),
(14, 'Literature', 'In which country does "Anna Karenina" take place?', 3),
(15, 'Literature', 'Who is the author of "To Kill a Mockingbird"?', 3);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(16, 'Movies', 'Which film won the first Academy Award for Best Picture?', 4),
(17, 'Movies', 'Who directed "Pulp Fiction"?', 4),
(18, 'Movies', 'What is the highest-grossing film of all time?', 4),
(19, 'Movies', 'Which movie features the quote, "I am going to make him an offer he cannot refuse"?', 4),
(20, 'Movies', 'Who played the role of Jack in "Titanic"?', 4);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(21, 'Music and Instruments', 'Who composed the Four Seasons?', 5),
(22, 'Music and Instruments', 'What instrument does Yo-Yo Ma famously play?', 5),
(23, 'Music and Instruments', 'Which genre of music originated in Jamaica?', 5),
(24, 'Music and Instruments', 'Who is known as the King of Pop?', 5),
(25, 'Music and Instruments', 'What is the musical term for playing softly?', 5);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(26, 'Computer Science', 'What does "HTTP" stand for?', 6),
(27, 'Computer Science', 'Who is considered the father of computer science?', 6),
(28, 'Computer Science', 'What is the binary system used for in computing?', 6),
(29, 'Computer Science', 'What is the name of the first computer virus?', 6),
(30, 'Computer Science', 'What language is primarily used for web development?', 6);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(31, 'Geography', 'Which country has the longest coastline?', 7),
(32, 'Geography', 'What is the capital of Australia?', 7),
(33, 'Geography', 'Which river is the longest in the world?', 7),
(34, 'Geography', 'Mount Everest is located in which country?', 7),
(35, 'Geography', 'What is the smallest country in the world?', 7);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(36, 'Sports', 'Which country won the 2018 FIFA World Cup?', 8),
(37, 'Sports', 'What sport does Serena Williams play?', 8),
(38, 'Sports', 'How many players are on a baseball team?', 8),
(39, 'Sports', 'What is the Olympic motto?', 8),
(40, 'Sports', 'In which sport is the Stanley Cup awarded?', 8);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(41, 'Art and Artists', 'Who painted the Mona Lisa?', 9),
(42, 'Art and Artists', 'What is the main period of Pablo Picasso?', 9),
(43, 'Art and Artists', 'Which artist is known for the style of Cubism?', 9),
(44, 'Art and Artists', 'What material is the sculpture "David" by Michelangelo made of?', 9),
(45, 'Art and Artists', 'Which museum houses Van Gogh "Starry Night"?', 9);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(46, 'Cooking and Food', 'What is traditionally the main ingredient in gazpacho?', 10),
(47, 'Cooking and Food', 'Which country is known for sushi?', 10),
(48, 'Cooking and Food', 'What type of food is Gouda?', 10),
(49, 'Cooking and Food', 'From which country does poutine originate?', 10),
(50, 'Cooking and Food', 'What is a common use for filo pastry?', 10);


-- add answers in the Answers Table in the quiz_sphere.db

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(1, 'Qin Shi Huang', 1, 1),
(2, 'Emperor Wu', 0, 1),
(3, 'Genghis Khan', 0, 1),
(4, 'King George', 0, 1),

(5, '1989', 1, 2),
(6, '1961', 0, 2),
(7, '1945', 0, 2),
(8, '1978', 0, 2),

(9, 'France', 1, 3),
(10, 'Canada', 0, 3),
(11, 'Germany', 0, 3),
(12, 'Italy', 0, 3),

(13, 'Assassination of Archduke Franz Ferdinand', 1, 4),
(14, 'Invention of the internet', 0, 4),
(15, 'Discovery of gold in Russia', 0, 4),
(16, 'The spread of communism', 0, 4),

(17, 'Christopher Columbus', 1, 5),
(18, 'Marco Polo', 0, 5),
(19, 'Vasco da Gama', 0, 5),
(20, 'Leif Erikson', 0, 5);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(21, 'Deoxyribonucleic Acid', 1, 6),
(22, 'Dynamic Nuclear Alignment', 0, 6),
(23, 'Distributed Network Application', 0, 6),
(24, 'Dual Node Access', 0, 6),

(25, 'Albert Einstein', 1, 7),
(26, 'Isaac Newton', 0, 7),
(27, 'Nikola Tesla', 0, 7),
(28, 'Marie Curie', 0, 7),

(29, 'Au', 1, 8),
(30, 'Ag', 0, 8),
(31, 'Pb', 0, 8),
(32, 'Fe', 0, 8),

(33, 'Alexander Graham Bell', 1, 9),
(34, 'Thomas Edison', 0, 9),
(35, 'Guglielmo Marconi', 0, 9),
(36, 'Nikola Tesla', 0, 9),

(37, '2006', 1, 10),
(38, '1999', 0, 10),
(39, '1988', 0, 10),
(40, '2001', 0, 10);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(41, 'George Orwell', 1, 11),
(42, 'Aldous Huxley', 0, 11),
(43, 'Ray Bradbury', 0, 11),
(44, 'Philip K. Dick', 0, 11),

(45, 'The American Dream', 1, 12),
(46, 'Love and Marriage', 0, 12),
(47, 'War and Peace', 0, 12),
(48, 'Technology and Modernization', 0, 12),

(49, 'A Midsummer Nights Dream', 1, 13),
(50, 'Hamlet', 0, 13),
(51, 'Macbeth', 0, 13),
(52, 'King Lear', 0, 13),

(53, 'Russia', 1, 14),
(54, 'France', 0, 14),
(55, 'Germany', 0, 14),
(56, 'Italy', 0, 14),

(57, 'Harper Lee', 1, 15),
(58, 'Truman Capote', 0, 15),
(59, 'J.D. Salinger', 0, 15),
(60, 'Stephen King', 0, 15);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(61, 'Wings', 1, 16),
(62, 'The Jazz Singer', 0, 16),
(63, 'Metropolis', 0, 16),
(64, 'Nosferatu', 0, 16),

(65, 'Quentin Tarantino', 1, 17),
(66, 'Steven Spielberg', 0, 17),
(67, 'Martin Scorsese', 0, 17),
(68, 'Stanley Kubrick', 0, 17),

(69, 'Avatar', 1, 18),
(70, 'Avengers: Endgame', 0, 18),
(71, 'Titanic', 0, 18),
(72, 'Star Wars: The Force Awakens', 0, 18),

(73, 'The Godfather', 1, 19),
(74, 'Goodfellas', 0, 19),
(75, 'The Sopranos', 0, 19),
(76, 'Casino', 0, 19),

(77, 'Leonardo DiCaprio', 1, 20),
(78, 'Brad Pitt', 0, 20),
(79, 'Johnny Depp', 0, 20),
(80, 'Tom Cruise', 0, 20);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(81, 'Antonio Vivaldi', 1, 21),
(82, 'Johann Sebastian Bach', 0, 21),
(83, 'Wolfgang Amadeus Mozart', 0, 21),
(84, 'Ludwig van Beethoven', 0, 21),

(85, 'Cello', 1, 22),
(86, 'Violin', 0, 22),
(87, 'Piano', 0, 22),
(88, 'Flute', 0, 22),

(89, 'Reggae', 1, 23),
(90, 'Blues', 0, 23),
(91, 'Jazz', 0, 23),
(92, 'Rock', 0, 23),

(93, 'Michael Jackson', 1, 24),
(94, 'Elvis Presley', 0, 24),
(95, 'Prince', 0, 24),
(96, 'Freddie Mercury', 0, 24),

(97, 'Piano', 1, 25),
(98, 'Forte', 0, 25),
(99, 'Crescendo', 0, 25),
(100, 'Staccato', 0, 25);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(101, 'Hypertext Transfer Protocol', 1, 26),
(102, 'High Transfer Text Protocol', 0, 26),
(103, 'Hyperlink Tracking Protocol', 0, 26),
(104, 'Hyper Transfer Protocol', 0, 26),

(105, 'Alan Turing', 1, 27),
(106, 'Charles Babbage', 0, 27),
(107, 'John von Neumann', 0, 27),
(108, 'Bill Gates', 0, 27),

(109, 'Storing data', 1, 28),
(110, 'Speed calculation', 0, 28),
(111, 'Enhancing graphics', 0, 28),
(112, 'Internet browsing', 0, 28),

(113, 'Elk Cloner', 1, 29),
(114, 'ILOVEYOU', 0, 29),
(115, 'MyDoom', 0, 29),
(116, 'Sasser', 0, 29),

(117, 'JavaScript', 1, 30),
(118, 'Python', 0, 30),
(119, 'C++', 0, 30),
(120, 'Java', 0, 30);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(121, 'Canada', 1, 31),
(122, 'Russia', 0, 31),
(123, 'China', 0, 31),
(124, 'USA', 0, 31),

(125, 'Canberra', 1, 32),
(126, 'Sydney', 0, 32),
(127, 'Melbourne', 0, 32),
(128, 'Perth', 0, 32),

(129, 'Nile', 1, 33),
(130, 'Amazon', 0, 33),
(131, 'Yangtze', 0, 33),
(132, 'Mississippi', 0, 33),

(133, 'Nepal', 1, 34),
(134, 'India', 0, 34),
(135, 'China', 0, 34),
(136, 'Bhutan', 0, 34),

(137, 'Vatican City', 1, 35),
(138, 'Monaco', 0, 35),
(139, 'Nauru', 0, 35),
(140, 'Tuvalu', 0, 35);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(141, 'France', 1, 36),
(142, 'Brazil', 0, 36),
(143, 'Germany', 0, 36),
(144, 'Argentina', 0, 36),

(145, 'Tennis', 1, 37),
(146, 'Golf', 0, 37),
(147, 'Basketball', 0, 37),
(148, 'Soccer', 0, 37),

(149, '9', 1, 38),
(150, '11', 0, 38),
(151, '7', 0, 38),
(152, '5', 0, 38),

(153, 'Faster, Higher, Stronger', 1, 39),
(154, 'Quick, Bold, Brave', 0, 39),
(155, 'Strong, Determined, Enduring', 0, 39),
(156, 'Brave, Bold, Beautiful', 0, 39),

(157, 'Ice Hockey', 1, 40),
(158, 'Basketball', 0, 40),
(159, 'Soccer', 0, 40),
(160, 'Cricket', 0, 40);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(161, 'Leonardo da Vinci', 1, 41),
(162, 'Vincent van Gogh', 0, 41),
(163, 'Claude Monet', 0, 41),
(164, 'Rembrandt', 0, 41),

(165, 'Cubism', 1, 43),
(166, 'Impressionism', 0, 43),
(167, 'Surrealism', 0, 43),
(168, 'Expressionism', 0, 43),

(169, 'Marble', 1, 44),
(170, 'Bronze', 0, 44),
(171, 'Wood', 0, 44),
(172, 'Clay', 0, 44),

(173, 'Museum of Modern Art, New York', 1, 45),
(174, 'Louvre Museum, Paris', 0, 45),
(175, 'Van Gogh Museum, Amsterdam', 0, 45),
(176, 'Prado Museum, Madrid', 0, 45);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(177, 'Tomato', 1, 46),
(178, 'Cucumber', 0, 46),
(179, 'Pepper', 0, 46),
(180, 'Onion', 0, 46),

(181, 'Japan', 1, 47),
(182, 'China', 0, 47),
(183, 'Korea', 0, 47),
(184, 'Thailand', 0, 47),

(185, 'Cheese', 1, 48),
(186, 'Bread', 0, 48),
(187, 'Sausage', 0, 48),
(188, 'Cake', 0, 48),

(189, 'Canada', 1, 49),
(190, 'USA', 0, 49),
(191, 'France', 0, 49),
(192, 'Germany', 0, 49),

(193, 'Making pastries', 1, 50),
(194, 'Thickening sauces', 0, 50),
(195, 'Frying', 0, 50),
(196, 'Salad dressing', 0, 50);

INSERT INTO Quizzes (id, title, description) VALUES
(1,'World History', )