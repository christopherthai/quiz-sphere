-- Quizz Subject(title)

INSERT INTO Quizzes (id, title, description) VALUES
(1, 'World History', 'World History'),
(2, 'Science Discoveries', 'Science Discoveries'),
(3, 'Literature','Literature'),
(4, 'Movies', 'Movies'),
(5, 'Music and Instruments', 'Music and Instruments'),
(6, 'Computer Science','Computer Science'),
(7, 'Geography','Geography'),
(8, 'Sports','Sports'),
(9, 'Art and Artists','Art and Artists'),
(10, 'Cooking and Food','Cooking and Food');

-- Users Scores

INSERT INTO Scores (id, score, date_taken, user_id, quiz_id) VALUES
(1, 92, '2024-02-18', 4, 1),
(2, 72, '2024-02-23', 4, 2),
(3, 92, '2024-02-07', 4, 3),
(4, 84, '2024-02-05', 4, 4),
(5, 99, '2024-01-18', 4, 5),
(6, 73, '2024-01-22', 4, 6),
(7, 96, '2024-02-18', 4, 7),
(8, 89, '2024-02-23', 4, 8),
(9, 80, '2024-02-07', 4, 9),
(10, 93, '2024-02-05', 4, 10),
(11, 92, '2024-02-18', 5, 1),
(12, 84, '2024-02-23', 5, 2),
(13, 76, '2024-02-07', 5, 3),
(14, 89, '2024-02-05', 5, 4),
(15, 93, '2024-01-18', 5, 5),
(16, 97, '2024-01-22', 5, 6),
(17, 91, '2024-02-18', 5, 7),
(18, 87, '2024-02-23', 5, 8),
(19, 81, '2024-02-07', 5, 9),
(20, 99, '2024-02-05', 5, 10),
(21, 71, '2024-02-18', 6, 1),
(22, 92, '2024-02-23', 6, 2),
(23, 69, '2024-02-07', 6, 3),
(24, 82, '2024-02-05', 6, 4),
(25, 93, '2024-01-18', 6, 5),
(26, 96, '2024-01-22', 6, 6),
(27, 95, '2024-02-18', 6, 7),
(28, 85, '2024-02-23', 6, 8),
(29, 71, '2024-02-07', 6, 9),
(30, 87, '2024-02-05', 6, 10),
(31, 89, '2024-02-18', 7, 1),
(32, 78, '2024-02-23', 7, 2),
(33, 96, '2024-02-07', 7, 3),
(34, 91, '2024-02-05', 7, 4),
(35, 86, '2024-01-18', 7, 5),
(36, 71, '2024-01-22', 7, 6),
(37, 91, '2024-02-18', 7, 7),
(38, 99, '2024-02-23', 7, 8),
(39, 85, '2024-02-07', 7, 9),
(40, 96, '2024-02-05', 7, 10),
(41, 92, '2024-02-18', 8, 1),
(42, 81, '2024-02-23', 8, 2),
(43, 73, '2024-02-07', 8, 3),
(44, 99, '2024-02-05', 8, 4),
(45, 83, '2024-01-18', 8, 5),
(46, 77, '2024-01-22', 8, 6),
(47, 92, '2024-02-18', 8, 7),
(48, 89, '2024-02-23', 8, 8),
(49, 88, '2024-02-07', 8, 9),
(50, 87, '2024-02-05', 8, 10),
(51, 78, '2024-02-18', 9, 1),
(52, 71, '2024-02-23', 9, 2),
(53, 89, '2024-02-07', 9, 3),
(54, 94, '2024-02-05', 9, 4),
(55, 90, '2024-01-18', 9, 5),
(56, 71, '2024-01-22', 9, 6),
(57, 81, '2024-02-18', 9, 7),
(58, 92, '2024-02-23', 9, 8),
(59, 85, '2024-02-07', 9, 9),
(60, 90, '2024-02-05', 9, 10),
(61, 99, '2024-02-18', 10, 1),
(62, 89, '2024-02-23', 10, 2),
(63, 91, '2024-02-07', 10, 3),
(64, 90, '2024-02-05', 10, 4),
(65, 71, '2024-01-18', 10, 5),
(66, 96, '2024-01-22', 10, 6),
(67, 99, '2024-02-18', 10, 7),
(68, 79, '2024-02-23', 10, 8),
(69, 85, '2024-02-07', 10, 9),
(70, 88, '2024-02-05', 10, 10),
(71, 85, '2024-02-18', 11, 1),
(72, 92, '2024-02-23', 11, 2),
(73, 82, '2024-02-07', 11, 3),
(74, 87, '2024-02-05', 11, 4),
(75, 96, '2024-01-18', 11, 5),
(76, 95, '2024-01-22', 11, 6),
(77, 84, '2024-02-18', 11, 7),
(78, 91, '2024-02-23', 11, 8),
(79, 89, '2024-02-07', 11, 9),
(80, 94, '2024-02-05', 11, 10),
(81, 79, '2024-02-18', 12, 1),
(82, 87, '2024-02-23', 12, 2),
(83, 85, '2024-02-07', 12, 3),
(84, 71, '2024-02-05', 12, 4),
(85, 90, '2024-01-18', 12, 5),
(86, 91, '2024-01-22', 12, 6),
(87, 93, '2024-02-18', 12, 7),
(88, 92, '2024-02-23', 12, 8),
(89, 83, '2024-02-07', 12, 9),
(90, 80, '2024-02-05', 12, 10),
(91, 96, '2024-02-18', 13, 1),
(92, 85, '2024-02-23', 13, 2),
(93, 90, '2024-02-07', 13, 3),
(94, 86, '2024-02-05', 13, 4),
(95, 89, '2024-01-18', 13, 5),
(96, 81, '2024-01-22', 13, 6),
(97, 71, '2024-02-18', 13, 7),
(98, 93, '2024-02-23', 13, 8),
(99, 94, '2024-02-07', 13, 9),
(100, 79, '2024-02-05', 13, 10);

-- Questions and Answers

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(1, 'World History', 'Who was the first emperor of China?', 1),
(2, 'World History', 'What year did the Berlin Wall fall?', 1),
(3, 'World History', 'Which country gifted the Statue of Liberty to the USA?', 1),
(4, 'World History', 'What was the main cause of World War I?', 1),
(5, 'World History', 'Who discovered America?', 1);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(6, 'Science Discoveries', 'What does DNA stand for?', 2),
(7, 'Science Discoveries', 'Who developed the theory of relativity?', 2),
(8, 'Science Discoveries', 'What is the chemical symbol for gold?', 2),
(9, 'Science Discoveries', 'Who invented the telephone?', 2),
(10, 'Science Discoveries', 'What year was Pluto reclassified as a dwarf planet?', 2);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(11, 'Literature', 'Who wrote "1984"?', 3),
(12, 'Literature', 'What is the main theme of "The Great Gatsby"?', 3),
(13, 'Literature', 'Which play by Shakespeare includes the character Puck?', 3),
(14, 'Literature', 'In which country does "Anna Karenina" take place?', 3),
(15, 'Literature', 'Who is the author of "To Kill a Mockingbird"?', 3);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(16, 'Movies', 'Which film won the first Academy Award for Best Picture?', 4),
(17, 'Movies', 'Who directed "Pulp Fiction"?', 4),
(18, 'Movies', 'What is the highest-grossing film of all time?', 4),
(19, 'Movies', 'Which movie features the quote, "I am going to make him an offer he cannot refuse"?', 4),
(20, 'Movies', 'Who played the role of Jack in "Titanic"?', 4);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(21, 'Music and Instruments', 'Who composed the Four Seasons?', 5),
(22, 'Music and Instruments', 'What instrument does Yo-Yo Ma famously play?', 5),
(23, 'Music and Instruments', 'Which genre of music originated in Jamaica?', 5),
(24, 'Music and Instruments', 'Who is known as the King of Pop?', 5),
(25, 'Music and Instruments', 'What is the musical term for playing softly?', 5);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(26, 'Computer Science', 'What does "HTTP" stand for?', 6),
(27, 'Computer Science', 'Who is considered the father of computer science?', 6),
(28, 'Computer Science', 'What is the binary system used for in computing?', 6),
(29, 'Computer Science', 'What is the name of the first computer virus?', 6),
(30, 'Computer Science', 'What language is primarily used for web development?', 6);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(31, 'Geography', 'Which country has the longest coastline?', 7),
(32, 'Geography', 'What is the capital of Australia?', 7),
(33, 'Geography', 'Which river is the longest in the world?', 7),
(34, 'Geography', 'Mount Everest is located in which country?', 7),
(35, 'Geography', 'What is the smallest country in the world?', 7);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(36, 'Sports', 'Which country won the 2018 FIFA World Cup?', 8),
(37, 'Sports', 'What sport does Serena Williams play?', 8),
(38, 'Sports', 'How many players are on a baseball team?', 8),
(39, 'Sports', 'What is the Olympic motto?', 8),
(40, 'Sports', 'In which sport is the Stanley Cup awarded?', 8);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(41, 'Art and Artists', 'Who painted the Mona Lisa?', 9),
(42, 'Art and Artists', 'What is the main period of Pablo Picasso?', 9),
(43, 'Art and Artists', 'Which artist is known for the style of Cubism?', 9),
(44, 'Art and Artists', 'What material is the sculpture "David" by Michelangelo made of?', 9),
(45, 'Art and Artists', 'Which museum houses Van Gogh "Starry Night"?', 9);

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

(197, 'Cubism', 1, 42),
(198, 'Baroque', 0, 42),
(199, 'Rococo', 0, 42),
(200, 'Surrealism', 0, 42),

(173, 'Museum of Modern Art, New York', 1, 45),
(174, 'Louvre Museum, Paris', 0, 45),
(175, 'Van Gogh Museum, Amsterdam', 0, 45),
(176, 'Prado Museum, Madrid', 0, 45);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(46, 'Cooking and Food', 'What is traditionally the main ingredient in gazpacho?', 10),
(47, 'Cooking and Food', 'Which country is known for sushi?', 10),
(48, 'Cooking and Food', 'What type of food is Gouda?', 10),
(49, 'Cooking and Food', 'From which country does poutine originate?', 10),
(50, 'Cooking and Food', 'What is a common use for filo pastry?', 10);

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

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(51, 'World History', 'Which ancient civilization built the pyramids?', 1),
(52, 'World History', 'What event marked the beginning of World War II in Europe?', 1),
(53, 'World History', 'Who was the first female Prime Minister of the United Kingdom?', 1),
(54, 'World History', 'What was the code name for the Allied invasion of Normandy in World War II?', 1),
(55, 'World History', 'Who was the first person to orbit the Earth?', 1);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(201, 'Egyptians', 1, 51),
(202, 'Greeks', 0, 51),
(203, 'Romans', 0, 51),
(204, 'Mayans', 0, 51);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(205, 'Assassination of Archduke Franz Ferdinand', 1, 52),
(206, 'Bombing of Pearl Harbor', 0, 52),
(207, 'Signing of the Treaty of Versailles', 0, 52),
(208, 'Invasion of Poland', 0, 52);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(209, 'Margaret Thatcher', 1, 53),
(210, 'Angela Merkel', 0, 53),
(211, 'Theresa May', 0, 53),
(212, 'Jacinda Ardern', 0, 53);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(213, 'Operation Overlord', 1, 54),
(214, 'Operation Barbarossa', 0, 54),
(215, 'Operation Market Garden', 0, 54),
(216, 'Operation Torch', 0, 54);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(217, 'Yuri Gagarin', 1, 55),
(218, 'Neil Armstrong', 0, 55),
(219, 'John Glenn', 0, 55),
(220, 'Buzz Aldrin', 0, 55);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(56, 'Science Discoveries', 'What is the smallest unit of matter?', 2),
(57, 'Science Discoveries', 'Who proposed the theory of evolution by natural selection?', 2),
(58, 'Science Discoveries', 'What is the formula for Einstein’s theory of mass-energy equivalence?', 2),
(59, 'Science Discoveries', 'Who discovered penicillin?', 2),
(60, 'Science Discoveries', 'What is the name of the largest particle accelerator in the world?', 2);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(221, 'Atom', 1, 56),
(222, 'Electron', 0, 56),
(223, 'Molecule', 0, 56),
(224, 'Cell', 0, 56);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(225, 'Charles Darwin', 1, 57),
(226, 'Isaac Newton', 0, 57),
(227, 'Albert Einstein', 0, 57),
(228, 'Gregor Mendel', 0, 57);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(229, 'E=mc^2', 1, 58),
(230, 'F=ma', 0, 58),
(231, 'PV=nRT', 0, 58),
(232, 'H2O', 0, 58);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(233, 'Alexander Fleming', 1, 59),
(234, 'Louis Pasteur', 0, 59),
(235, 'Robert Koch', 0, 59),
(236, 'Jonas Salk', 0, 59);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(237, 'Large Hadron Collider', 1, 60),
(238, 'Tevatron', 0, 60),
(239, 'Relativistic Heavy Ion Collider', 0, 60),
(240, 'Linac Coherent Light Source', 0, 60);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(61, 'Literature', 'Which author wrote "The Catcher in the Rye"?', 3),
(62, 'Literature', 'What is the famous opening line of "Moby-Dick"?', 3),
(63, 'Literature', 'In which novel would you find the character Holden Caulfield?', 3),
(64, 'Literature', 'Who wrote the play "Romeo and Juliet"?', 3),
(65, 'Literature', 'What is the full title of Charles Dickens novel "Oliver Twist"?', 3);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(241, 'J.D. Salinger', 1, 61),
(242, 'Ernest Hemingway', 0, 61),
(243, 'F. Scott Fitzgerald', 0, 61),
(244, 'Mark Twain', 0, 61);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(245, 'Call me Ishmael', 1, 62),
(246, 'It was the best of times, it was the worst of times', 0, 62),
(247, 'All happy families are alike; each unhappy family is unhappy in its own way', 0, 62),
(248, 'Happy families are all alike; every unhappy family is unhappy in its own way', 0, 62);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(249, 'The Catcher in the Rye', 1, 63),
(250, 'Lord of the Flies', 0, 63),
(251, 'To Kill a Mockingbird', 0, 63),
(252, 'The Grapes of Wrath', 0, 63);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(253, 'William Shakespeare', 1, 64),
(254, 'Jane Austen', 0, 64),
(255, 'Charles Dickens', 0, 64),
(256, 'Leo Tolstoy', 0, 64);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(257, 'Oliver Twist or the Parish Boys Progress', 1, 65),
(258, 'Great Expectations', 0, 65),
(259, 'David Copperfield', 0, 65),
(260, 'A Tale of Two Cities', 0, 65);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(66, 'Movies', 'Who directed the movie "Schindlers List"?', 4),
(67, 'Movies', 'Which movie features the character Hannibal Lecter?', 4),
(68, 'Movies', 'Who played the role of Forrest Gump in the movie of the same name?', 4),
(69, 'Movies', 'What is the highest-grossing animated film of all time?', 4),
(70, 'Movies', 'Which movie won the Academy Award for Best Picture in 2020?', 4);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(261, 'Steven Spielberg', 1, 66),
(262, 'Quentin Tarantino', 0, 66),
(263, 'Martin Scorsese', 0, 66),
(264, 'Francis Ford Coppola', 0, 66);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(265, 'The Silence of the Lambs', 1, 67),
(266, 'Se7en', 0, 67),
(267, 'The Usual Suspects', 0, 67),
(268, 'Fight Club', 0, 67);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(269, 'Tom Hanks', 1, 68),
(270, 'Brad Pitt', 0, 68),
(271, 'Leonardo DiCaprio', 0, 68),
(272, 'Matt Damon', 0, 68);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(273, 'Frozen II', 1, 69),
(274, 'The Lion King', 0, 69),
(275, 'Avengers: Endgame', 0, 69),
(276, 'Avatar', 0, 69);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(277, 'Parasite', 1, 70),
(278, 'Nomadland', 0, 70),
(279, 'Joker', 0, 70),
(280, 'The Shape of Water', 0, 70);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(71, 'Music and Instruments', 'Which composer is known as the "Waltz King"?', 5),
(72, 'Music and Instruments', 'What instrument does Kenny G play?', 5),
(73, 'Music and Instruments', 'Which band released the album "The Dark Side of the Moon"?', 5),
(74, 'Music and Instruments', 'Who sang the hit song "Imagine"?', 5),
(75, 'Music and Instruments', 'What is the highest male singing voice?', 5);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(281, 'Johann Strauss II', 1, 71),
(282, 'Wolfgang Amadeus Mozart', 0, 71),
(283, 'Ludwig van Beethoven', 0, 71),
(284, 'Frédéric Chopin', 0, 71);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(285, 'Saxophone', 1, 72),
(286, 'Piano', 0, 72),
(287, 'Trumpet', 0, 72),
(288, 'Guitar', 0, 72);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(289, 'Pink Floyd', 1, 73),
(290, 'The Beatles', 0, 73),
(291, 'Led Zeppelin', 0, 73),
(292, 'The Rolling Stones', 0, 73);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(293, 'John Lennon', 1, 74),
(294, 'Paul McCartney', 0, 74),
(295, 'David Bowie', 0, 74),
(296, 'Elton John', 0, 74);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(297, 'Countertenor', 1, 75),
(298, 'Tenor', 0, 75),
(299, 'Baritone', 0, 75),
(300, 'Bass', 0, 75);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(76, 'Computer Science', 'What programming language was created by Guido van Rossum?', 6),
(77, 'Computer Science', 'What is the most popular operating system for web servers?', 6),
(78, 'Computer Science', 'What does the acronym "SQL" stand for?', 6),
(79, 'Computer Science', 'Who invented the World Wide Web?', 6),
(80, 'Computer Science', 'What is the function of a compiler?', 6);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(301, 'Python', 1, 76),
(302, 'Java', 0, 76),
(303, 'C++', 0, 76),
(304, 'JavaScript', 0, 76);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(305, 'Linux', 1, 77),
(306, 'Windows', 0, 77),
(307, 'macOS', 0, 77),
(308, 'iOS', 0, 77);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(309, 'Structured Query Language', 1, 78),
(310, 'Simple Query Language', 0, 78),
(311, 'Server Query Language', 0, 78),
(312, 'Sequential Query Language', 0, 78);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(313, 'Tim Berners-Lee', 1, 79),
(314, 'Bill Gates', 0, 79),
(315, 'Steve Jobs', 0, 79),
(316, 'Mark Zuckerberg', 0, 79);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(317, 'Translate high-level code into machine code', 1, 80),
(318, 'Manage computer resources', 0, 80),
(319, 'Store data permanently', 0, 80),
(320, 'Connect to the internet', 0, 80);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(81, 'Geography', 'Which desert is the largest in the world?', 7),
(82, 'Geography', 'What is the tallest mountain in Africa?', 7),
(83, 'Geography', 'Which continent is the least populated?', 7),
(84, 'Geography', 'What is the capital of Canada?', 7),
(85, 'Geography', 'Which river runs through Baghdad?', 7);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(321, 'Antarctica', 1, 81),
(322, 'Arctic', 0, 81),
(323, 'Sahara', 0, 81),
(324, 'Gobi', 0, 81);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(325, 'Mount Kilimanjaro', 1, 82),
(326, 'Mount Everest', 0, 82),
(327, 'Mount Fuji', 0, 82),
(328, 'Mount Elbrus', 0, 82);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(329, 'Antarctica', 1, 83),
(330, 'Africa', 0, 83),
(331, 'Australia', 0, 83),
(332, 'South America', 0, 83);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(333, 'Ottawa', 1, 84),
(334, 'Toronto', 0, 84),
(335, 'Vancouver', 0, 84),
(336, 'Montreal', 0, 84);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(337, 'Tigris', 1, 85),
(338, 'Nile', 0, 85),
(339, 'Amazon', 0, 85),
(340, 'Yangtze', 0, 85);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(86, 'Sports', 'What is the highest possible score in a gymnastics routine?', 8),
(87, 'Sports', 'In what year were the first modern Olympic Games held?', 8),
(88, 'Sports', 'Which country hosted the 2016 Summer Olympics?', 8),
(89, 'Sports', 'Who is the all-time leading goal scorer in FIFA World Cup history?', 8),
(90, 'Sports', 'In what year were women allowed to participate in the modern Olympic Games?', 8);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(341, '10', 1, 86),
(342, '9.5', 0, 86),
(343, '15', 0, 86),
(344, '20', 0, 86);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(345, '1896', 1, 87),
(346, '1900', 0, 87),
(347, '1888', 0, 87),
(348, '1912', 0, 87);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(349, 'Brazil', 1, 88),
(350, 'China', 0, 88),
(351, 'Russia', 0, 88),
(352, 'Australia', 0, 88);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(353, 'Miroslav Klose', 1, 89),
(354, 'Pele', 0, 89),
(355, 'Ronaldo', 0, 89),
(356, 'Diego Maradona', 0, 89);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(357, '1900', 1, 90),
(358, '1896', 0, 90),
(359, '1920', 0, 90),
(360, '1936', 0, 90);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(91, 'Art and Artists', 'Which artist is famous for painting the "Girl with a Pearl Earring"?', 9),
(92, 'Art and Artists', 'Who designed the iconic glass pyramid at the entrance of the Louvre Museum in Paris?', 9),
(93, 'Art and Artists', 'Which art movement did Salvador Dalí belong to?', 9),
(94, 'Art and Artists', 'What is the name of the famous sculpture depicting the Greek goddess of love and beauty?', 9),
(95, 'Art and Artists', 'Which Italian artist is known for his sculptural masterpiece "David"?', 9);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(361, 'Johannes Vermeer', 1, 91),
(362, 'Vincent van Gogh', 0, 91),
(363, 'Rembrandt', 0, 91),
(364, 'Pablo Picasso', 0, 91);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(365, 'I. M. Pei', 1, 92),
(366, 'Frank Gehry', 0, 92),
(367, 'Renzo Piano', 0, 92),
(368, 'Zaha Hadid', 0, 92);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(369, 'Surrealism', 1, 93),
(370, 'Impressionism', 0, 93),
(371, 'Cubism', 0, 93),
(372, 'Expressionism', 0, 93);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(373, 'Venus de Milo', 1, 94),
(374, 'The Winged Victory of Samothrace', 0, 94),
(375, 'Discobolus', 0, 94),
(376, 'Laocoön and His Sons', 0, 94);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(377, 'Michelangelo', 1, 95),
(378, 'Donatello', 0, 95),
(379, 'Leonardo da Vinci', 0, 95),
(380, 'Raphael', 0, 95);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(96, 'Cooking and Food', 'Which country is the origin of paella?', 10),
(97, 'Cooking and Food', 'What is the primary ingredient in hummus?', 10),
(98, 'Cooking and Food', 'What type of cuisine is kimchi associated with?', 10),
(99, 'Cooking and Food', 'What is the main ingredient in a traditional Caprese salad?', 10),
(100, 'Cooking and Food', 'What is the national dish of Japan?', 10);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(381, 'Spain', 1, 96),
(382, 'Italy', 0, 96),
(383, 'Portugal', 0, 96),
(384, 'France', 0, 96);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(385, 'Chickpeas', 1, 97),
(386, 'Lentils', 0, 97),
(387, 'Tahini', 0, 97),
(388, 'Eggplant', 0, 97);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(389, 'Korean', 1, 98),
(390, 'Japanese', 0, 98),
(391, 'Chinese', 0, 98),
(392, 'Thai', 0, 98);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(393, 'Tomatoes', 1, 99),
(394, 'Mozzarella', 0, 99),
(395, 'Basil', 0, 99),
(396, 'Olive oil', 0, 99);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(397, 'Sushi', 1, 100),
(398, 'Ramen', 0, 100),
(399, 'Tempura', 0, 100),
(400, 'Teriyaki', 0, 100);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(101, 'World History', 'What empire was known as "the empire on which the sun never sets"?', 1),
(102, 'World History', 'In which year did the American Revolutionary War begin?', 1),
(103, 'World History', 'Who was the Pharaoh of Egypt during the Exodus?', 1),
(104, 'World History', 'What ancient civilization invented the wheel?', 1),
(105, 'World History', 'Which treaty ended the Thirty Years'' War?', 1),
(106, 'World History', 'Who was the Russian leader during the Cuban Missile Crisis?', 1),
(107, 'World History', 'What was the capital of the Inca Empire?', 1),
(108, 'World History', 'Which city was the first to be attacked with an atomic bomb?', 1),
(109, 'World History', 'Who led the Norman conquest of England?', 1),
(110, 'World History', 'What was the main trading route between the East and West called in the Middle Ages?', 1);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(401, 'British Empire', 1, 101),
(402, 'France', 0, 101),
(403, 'Germany', 0, 101),
(404, 'Portugal', 0, 101),
(405, '1775', 1, 102),
(406, '1776', 0, 102),
(407, '1781', 0, 102),
(408, '1765', 0, 102),
(409, 'Ramses II', 1, 103),
(410, 'Tutankhamun', 0, 103),
(411, 'Cleopatra', 0, 103),
(412, 'Nefertiti', 0, 103),
(413, 'Sumerians', 1, 104),
(414, 'Egyptians', 0, 104),
(415, 'Greeks', 0, 104),
(416, 'Romans', 0, 104),
(417, 'Peace of Westphalia', 1, 105),
(418, 'Treaty of Versailles', 0, 105),
(419, 'Magna Carta', 0, 105),
(420, 'Treaty of Tordesillas', 0, 105),
(421, 'Nikita Khrushchev', 1, 106),
(422, 'Joseph Stalin', 0, 106),
(423, 'Vladimir Lenin', 0, 106),
(424, 'Leonid Brezhnev', 0, 106),
(425, 'Cusco', 1, 107),
(426, 'Machu Picchu', 0, 107),
(427, 'Lima', 0, 107),
(428, 'Quito', 0, 107),
(429, 'Hiroshima', 1, 108),
(430, 'Nagasaki', 0, 108),
(431, 'Tokyo', 0, 108),
(432, 'Osaka', 0, 108),
(433, 'William the Conqueror', 1, 109),
(434, 'Henry VIII', 0, 109),
(435, 'Edward I', 0, 109),
(436, 'Richard the Lionheart', 0, 109),
(437, 'Silk Road', 1, 110),
(438, 'Amber Road', 0, 110),
(439, 'Spice Route', 0, 110),
(440, 'Tea Route', 0, 110);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(111, 'Science Discoveries', 'What element has the highest melting point?', 2),
(112, 'Science Discoveries', 'Which planet is known as the "Morning Star"?', 2),
(113, 'Science Discoveries', 'What is the powerhouse of the cell?', 2),
(114, 'Science Discoveries', 'Who discovered the circulation of blood?', 2),
(115, 'Science Discoveries', 'What is the most abundant gas in the Earth''s atmosphere?', 2),
(116, 'Science Discoveries', 'Who first observed the moons of Jupiter?', 2),
(117, 'Science Discoveries', 'What particle is known for its uncertainty in position and momentum?', 2),
(118, 'Science Discoveries', 'Which vitamin is produced by the human skin in response to sunlight?', 2),
(119, 'Science Discoveries', 'What is the term for the number of species living within an ecosystem?', 2),
(120, 'Science Discoveries', 'What is the hardest natural substance on Earth?', 2);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(441, 'Tungsten', 1, 111),
(442, 'Iron', 0, 111),
(443, 'Gold', 0, 111),
(444, 'Silver', 0, 111),
(445, 'Venus', 1, 112),
(446, 'Mars', 0, 112),
(447, 'Jupiter', 0, 112),
(448, 'Saturn', 0, 112),
(449, 'Mitochondrion', 1, 113),
(450, 'Nucleus', 0, 113),
(451, 'Ribosome', 0, 113),
(452, 'Endoplasmic reticulum', 0, 113),
(453, 'William Harvey', 1, 114),
(454, 'Isaac Newton', 0, 114),
(455, 'Galileo Galilei', 0, 114),
(456, 'Robert Hooke', 0, 114),
(457, 'Nitrogen', 1, 115),
(458, 'Oxygen', 0, 115),
(459, 'Carbon dioxide', 0, 115),
(460, 'Helium', 0, 115),
(461, 'Galileo Galilei', 1, 116),
(462, 'Copernicus', 0, 116),
(463, 'Kepler', 0, 116),
(464, 'Hubble', 0, 116),
(465, 'Electron', 1, 117),
(466, 'Proton', 0, 117),
(467, 'Neutron', 0, 117),
(468, 'Photon', 0, 117),
(469, 'Vitamin D', 1, 118),
(470, 'Vitamin C', 0, 118),
(471, 'Vitamin A', 0, 118),
(472, 'Vitamin E', 0, 118),
(473, 'Biodiversity', 1, 119),
(474, 'Biomass', 0, 119),
(475, 'Biome', 0, 119),
(476, 'Bioactivity', 0, 119),
(477, 'Diamond', 1, 120),
(478, 'Quartz', 0, 120),
(479, 'Ruby', 0, 120),
(480, 'Sapphire', 0, 120);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(121, 'Literature', 'Who wrote "Pride and Prejudice"?', 3),
(122, 'Literature', 'In which century was "Don Quixote" written?', 3),
(123, 'Literature', 'Which novel features a character named Jay Gatsby?', 3),
(124, 'Literature', 'What is the title of the sequel to "To Kill a Mockingbird"?', 3),
(125, 'Literature', 'Which poet wrote "The Road Not Taken"?', 3),
(126, 'Literature', 'What is the fictional language created in "A Clockwork Orange"?', 3),
(127, 'Literature', 'Who wrote the epic poem "Paradise Lost"?', 3),
(128, 'Literature', 'In which novel can you find the character Elizabeth Bennet?', 3),
(129, 'Literature', 'What genre is associated with Edgar Allan Poe?', 3),
(130, 'Literature', 'Which author created the character Sherlock Holmes?', 3);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(481, 'Jane Austen', 1, 121),
(482, 'Charlotte Bronte', 0, 121),
(483, 'Emily Bronte', 0, 121),
(484, 'Mary Shelley', 0, 121),
(485, '16th Century', 1, 122),
(486, '17th Century', 0, 122),
(487, '18th Century', 0, 122),
(488, '15th Century', 0, 122),
(489, 'The Great Gatsby', 1, 123),
(490, 'The Catcher in the Rye', 0, 123),
(491, 'The Old Man and the Sea', 0, 123),
(492, '1984', 0, 123),
(493, 'Go Set a Watchman', 1, 124),
(494, 'The Long Goodbye', 0, 124),
(495, 'Catcher in the Rye', 0, 124),
(496, 'Brave New World', 0, 124),
(497, 'Robert Frost', 1, 125),
(498, 'Walt Whitman', 0, 125),
(499, 'T.S. Eliot', 0, 125),
(500, 'Langston Hughes', 0, 125),
(501, 'Nadsat', 1, 126),
(502, 'Klingon', 0, 126),
(503, 'Dothraki', 0, 126),
(504, 'Elvish', 0, 126),
(505, 'John Milton', 1, 127),
(506, 'Homer', 0, 127),
(507, 'Virgil', 0, 127),
(508, 'Dante', 0, 127),
(509, 'Pride and Prejudice', 1, 128),
(510, 'Wuthering Heights', 0, 128),
(511, 'Jane Eyre', 0, 128),
(512, 'Little Women', 0, 128),
(513, 'Gothic', 1, 129),
(514, 'Romantic', 0, 129),
(515, 'Realism', 0, 129),
(516, 'Modernism', 0, 129),
(517, 'Arthur Conan Doyle', 1, 130),
(518, 'Agatha Christie', 0, 130),
(519, 'Ian Fleming', 0, 130),
(520, 'J.K. Rowling', 0, 130);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(131, 'Movies', 'Which movie features a famous dance scene on a large piano?', 3),
(132, 'Movies', 'Who starred as the lead in the original "Blade Runner"?', 3),
(133, 'Movies', 'What year was the movie "Jurassic Park" released?', 3),
(134, 'Movies', 'Which film features the fictional sport of Quidditch?', 3),
(135, 'Movies', 'What is the name of the ship in the movie "Titanic"?', 3),
(136, 'Movies', 'Who directed "Avatar"?', 3),
(137, 'Movies', 'Which movie won the Best Picture Oscar in 1994?', 3),
(138, 'Movies', 'What fictional city is the home of Batman?', 3),
(139, 'Movies', 'In which movie did Leonardo DiCaprio say the line, "I am the king of the world!"?', 3),
(140, 'Movies', 'Who played the role of Neo in "The Matrix"?', 3);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(521, 'Big', 1, 131),
(522, 'Footloose', 0, 131),
(523, 'Dirty Dancing', 0, 131),
(524, 'Flashdance', 0, 131),
(525, 'Harrison Ford', 1, 132),
(526, 'Sean Connery', 0, 132),
(527, 'Bruce Willis', 0, 132),
(528, 'Arnold Schwarzenegger', 0, 132),
(529, '1993', 1, 133),
(530, '1995', 0, 133),
(531, '1990', 0, 133),
(532, '1989', 0, 133),
(533, 'Harry Potter and the Sorcerer''s Stone', 1, 134),
(534, 'The Hunger Games', 0, 134),
(535, 'Ender''s Game', 0, 134),
(536, 'Star Wars: Episode I', 0, 134),
(537, 'RMS Titanic', 1, 135),
(538, 'USS Enterprise', 0, 135),
(539, 'The Black Pearl', 0, 135),
(540, 'Nautilus', 0, 135),
(541, 'James Cameron', 1, 136),
(542, 'Steven Spielberg', 0, 136),
(543, 'George Lucas', 0, 136),
(544, 'Ridley Scott', 0, 136),
(545, 'Forrest Gump', 1, 137),
(546, 'Pulp Fiction', 0, 137),
(547, 'The Shawshank Redemption', 0, 137),
(548, 'Jurassic Park', 0, 137),
(549, 'Gotham', 1, 138),
(550, 'Metropolis', 0, 138),
(551, 'Central City', 0, 138),
(552, 'Star City', 0, 138),
(553, 'Titanic', 1, 139),
(554, 'Inception', 0, 139),
(555, 'The Great Gatsby', 0, 139),
(556, 'Shutter Island', 0, 139),
(557, 'Keanu Reeves', 1, 140),
(558, 'Brad Pitt', 0, 140),
(559, 'Johnny Depp', 0, 140),
(560, 'Tom Cruise', 0, 140);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(141, 'Music and Instruments', 'What is the name of the instrument primarily used in Flamenco music?', 5),
(142, 'Music and Instruments', 'Who wrote the opera "The Magic Flute"?', 5),
(143, 'Music and Instruments', 'Which musician is famous for playing the electric guitar solo on "Stairway to Heaven"?', 5),
(144, 'Music and Instruments', 'What type of voice is higher than tenor?', 5),
(145, 'Music and Instruments', 'Which famous jazz musician was known as "Satchmo"?', 5),
(146, 'Music and Instruments', 'What instrument is Robert Plant known for playing?', 5),
(147, 'Music and Instruments', 'Which musical key features no sharps or flats?', 5),
(148, 'Music and Instruments', 'Who is credited with inventing the solid-body electric guitar?', 5),
(149, 'Music and Instruments', 'What is the Italian term for gradually speeding up the tempo?', 5),
(150, 'Music and Instruments', 'Who composed "Moonlight Sonata"?', 5);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(561, 'Guitar', 1, 141),
(562, 'Violin', 0, 141),
(563, 'Piano', 0, 141),
(564, 'Saxophone', 0, 141),
(565, 'Wolfgang Amadeus Mozart', 1, 142),
(566, 'Ludwig van Beethoven', 0, 142),
(567, 'Johann Sebastian Bach', 0, 142),
(568, 'Giuseppe Verdi', 0, 142),
(569, 'Jimmy Page', 1, 143),
(570, 'Eric Clapton', 0, 143),
(571, 'Jimi Hendrix', 0, 143),
(572, 'David Gilmour', 0, 143),
(573, 'Countertenor', 1, 144),
(574, 'Baritone', 0, 144),
(575, 'Bass', 0, 144),
(576, 'Alto', 0, 144),
(577, 'Louis Armstrong', 1, 145),
(578, 'Duke Ellington', 0, 145),
(579, 'Charlie Parker', 0, 145),
(580, 'Miles Davis', 0, 145),
(581, 'None (He is a vocalist)', 1, 146),
(582, 'Guitar', 0, 146),
(583, 'Drums', 0, 146),
(584, 'Harmonica', 0, 146),
(585, 'C Major', 1, 147),
(586, 'G Major', 0, 147),
(587, 'E Minor', 0, 147),
(588, 'B Flat Major', 0, 147),
(589, 'Les Paul', 1, 148),
(590, 'Leo Fender', 0, 148),
(591, 'Orville Gibson', 0, 148),
(592, 'Adolph Rickenbacker', 0, 148),
(593, 'Accelerando', 1, 149),
(594, 'Andante', 0, 149),
(595, 'Adagio', 0, 149),
(596, 'Allegro', 0, 149),
(597, 'Ludwig van Beethoven', 1, 150),
(598, 'Wolfgang Amadeus Mozart', 0, 150),
(599, 'Franz Schubert', 0, 150),
(600, 'Johannes Brahms', 0, 150);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(151, 'Computer Science', 'Which data structure uses a FIFO method?', 6),
(152, 'Computer Science', 'What does "AI" stand for in technology?', 6),
(153, 'Computer Science', 'What is the main advantage of using cloud computing?', 6),
(154, 'Computer Science', 'Which language is known for its use in artificial intelligence and machine learning?', 6),
(155, 'Computer Science', 'What protocol is primarily used for sending email?', 6),
(156, 'Computer Science', 'Which device converts digital signals to analog signals and vice versa?', 6),
(157, 'Computer Science', 'What is a common method for securing transmitted data?', 6),
(158, 'Computer Science', 'Who is credited with creating Linux?', 6),
(159, 'Computer Science', 'What does GPU stand for?', 6),
(160, 'Computer Science', 'What is the standard markup language used to create web pages?', 6);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(601, 'Queue', 1, 151),
(602, 'Stack', 0, 151),
(603, 'Array', 0, 151),
(604, 'Graph', 0, 151),
(605, 'Artificial Intelligence', 1, 152),
(606, 'Automated Input', 0, 152),
(607, 'Application Interface', 0, 152),
(608, 'Automated Intelligence', 0, 152),
(609, 'Scalability', 1, 153),
(610, 'Cost', 0, 153),
(611, 'Speed', 0, 153),
(612, 'Security', 0, 153),
(613, 'Python', 1, 154),
(614, 'Java', 0, 154),
(615, 'C++', 0, 154),
(616, 'Ruby', 0, 154),
(617, 'SMTP', 1, 155),
(618, 'HTTP', 0, 155),
(619, 'FTP', 0, 155),
(620, 'TCP', 0, 155),
(621, 'Modem', 1, 156),
(622, 'Router', 0, 156),
(623, 'Switch', 0, 156),
(624, 'Repeater', 0, 156),
(625, 'Encryption', 1, 157),
(626, 'Tokenization', 0, 157),
(627, 'Compression', 0, 157),
(628, 'Redaction', 0, 157),
(629, 'Linus Torvalds', 1, 158),
(630, 'Bill Gates', 0, 158),
(631, 'Steve Jobs', 0, 158),
(632, 'Mark Zuckerberg', 0, 158),
(633, 'Graphics Processing Unit', 1, 159),
(634, 'Graphical Programming Unit', 0, 159),
(635, 'General Processing Unit', 0, 159),
(636, 'Graphics Performance Unit', 0, 159),
(637, 'HTML', 1, 160),
(638, 'XML', 0, 160),
(639, 'SGML', 0, 160),
(640, 'CSS', 0, 160);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(161, 'Geography', 'Which river flows through Paris?', 7),
(162, 'Geography', 'What is the largest island in the world?', 7),
(163, 'Geography', 'Which country has the most natural lakes?', 7),
(164, 'Geography', 'What is the smallest continent by land area?', 7),
(165, 'Geography', 'Which U.S. state has the longest coastline?', 7),
(166, 'Geography', 'Which continent contains the most countries?', 7),
(167, 'Geography', 'What is the capital of Brazil?', 7),
(168, 'Geography', 'Which African nation is completely surrounded by South Africa?', 7),
(169, 'Geography', 'Which mountain range separates Europe and Asia?', 7),
(170, 'Geography', 'What is the oldest active volcano on Earth?', 7);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(641, 'Seine', 1, 161),
(642, 'Thames', 0, 161),
(643, 'Danube', 0, 161),
(644, 'Rhine', 0, 161),
(645, 'Greenland', 1, 162),
(646, 'Iceland', 0, 162),
(647, 'New Guinea', 0, 162),
(648, 'Madagascar', 0, 162),
(649, 'Canada', 1, 163),
(650, 'Russia', 0, 163),
(651, 'China', 0, 163),
(652, 'Brazil', 0, 163),
(653, 'Australia', 1, 164),
(654, 'Antarctica', 0, 164),
(655, 'Europe', 0, 164),
(656, 'South America', 0, 164),
(657, 'Alaska', 1, 165),
(658, 'California', 0, 165),
(659, 'Florida', 0, 165),
(660, 'Texas', 0, 165),
(661, 'Africa', 1, 166),
(662, 'Europe', 0, 166),
(663, 'Asia', 0, 166),
(664, 'South America', 0, 166),
(665, 'Brasilia', 1, 167),
(666, 'Rio de Janeiro', 0, 167),
(667, 'São Paulo', 0, 167),
(668, 'Salvador', 0, 167),
(669, 'Lesotho', 1, 168),
(670, 'Swaziland', 0, 168),
(671, 'Botswana', 0, 168),
(672, 'Namibia', 0, 168),
(673, 'Ural Mountains', 1, 169),
(674, 'Andes', 0, 169),
(675, 'Himalayas', 0, 169),
(676, 'Rocky Mountains', 0, 169),
(677, 'Mount Etna', 1, 170),
(678, 'Mount Vesuvius', 0, 170),
(679, 'Mount Fuji', 0, 170),
(680, 'Mauna Loa', 0, 170);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(171, 'Sports', 'Which sport is known as the "king of sports"?', 8),
(172, 'Sports', 'Who holds the record for the most Olympic gold medals?', 8),
(173, 'Sports', 'What is the official national sport of Japan?', 8),
(174, 'Sports', 'Which country won the most recent FIFA World Cup?', 8),
(175, 'Sports', 'In tennis, what is a zero score called?', 8),
(176, 'Sports', 'Which sport uses terms like "stale fish" and "ollie"?', 8),
(177, 'Sports', 'What is the maximum score in a single frame of bowling?', 8),
(178, 'Sports', 'Which athlete is known as "The Great One" in ice hockey?', 8),
(179, 'Sports', 'What is the distance of a marathon?', 8),
(180, 'Sports', 'Which sport awards the Claret Jug?', 8);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(681, 'Soccer', 1, 171),
(682, 'Basketball', 0, 171),
(683, 'Cricket', 0, 171),
(684, 'Baseball', 0, 171),
(685, 'Michael Phelps', 1, 172),
(686, 'Usain Bolt', 0, 172),
(687, 'Larisa Latynina', 0, 172),
(688, 'Mark Spitz', 0, 172),
(689, 'Sumo Wrestling', 1, 173),
(690, 'Judo', 0, 173),
(691, 'Karate', 0, 173),
(692, 'Kendo', 0, 173),
(693, 'France', 1, 174),
(694, 'Brazil', 0, 174),
(695, 'Germany', 0, 174),
(696, 'Argentina', 0, 174),
(697, 'Love', 1, 175),
(698, 'Nil', 0, 175),
(699, 'Zero', 0, 175),
(700, 'Goose egg', 0, 175),
(701, 'Snowboarding', 1, 176),
(702, 'Surfing', 0, 176),
(703, 'Skateboarding', 0, 176),
(704, 'BMX', 0, 176),
(705, '300', 1, 177),
(706, '200', 0, 177),
(707, '100', 0, 177),
(708, '400', 0, 177),
(709, 'Wayne Gretzky', 1, 178),
(710, 'Bobby Orr', 0, 178),
(711, 'Mario Lemieux', 0, 178),
(712, 'Gordie Howe', 0, 178),
(713, '26.2 miles', 1, 179),
(714, '13.1 miles', 0, 179),
(715, '100 kilometers', 0, 179),
(716, '42.2 kilometers', 0, 179),
(717, 'Golf', 1, 180),
(718, 'Tennis', 0, 180),
(719, 'Cricket', 0, 180),
(720, 'Rugby', 0, 180);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(181, 'Art and Artists', 'Who painted "The Night Watch"?', 9),
(182, 'Art and Artists', 'Which artist sculpted "The Thinker"?', 9),
(183, 'Art and Artists', 'What is the primary period of Rembrandt''s art?', 9),
(184, 'Art and Artists', 'Who is known for the pop art piece "Marilyn Diptych"?', 9),
(185, 'Art and Artists', 'Which artist is associated with the phrase "Blue Period"?', 9),
(186, 'Art and Artists', 'What famous painting resides in the Sistine Chapel?', 9),
(187, 'Art and Artists', 'Who designed the Vietnam Veterans Memorial in Washington, D.C.?', 9),
(188, 'Art and Artists', 'Which movement is Wassily Kandinsky associated with?', 9),
(189, 'Art and Artists', 'Who painted "The School of Athens"?', 9),
(190, 'Art and Artists', 'Which artist is famous for the painting "The Persistence of Memory"?', 9);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(721, 'Rembrandt', 1, 181),
(722, 'Vermeer', 0, 181),
(723, 'Van Gogh', 0, 181),
(724, 'Picasso', 0, 181),
(725, 'Auguste Rodin', 1, 182),
(726, 'Michelangelo', 0, 182),
(727, 'Donatello', 0, 182),
(728, 'Bernini', 0, 182),
(729, 'Baroque', 1, 183),
(730, 'Renaissance', 0, 183),
(731, 'Impressionism', 0, 183),
(732, 'Modernism', 0, 183),
(733, 'Andy Warhol', 1, 184),
(734, 'Roy Lichtenstein', 0, 184),
(735, 'Jackson Pollock', 0, 184),
(736, 'Jean-Michel Basquiat', 0, 184),
(737, 'Pablo Picasso', 1, 185),
(738, 'Claude Monet', 0, 185),
(739, 'Henri Matisse', 0, 185),
(740, 'Salvador Dalí', 0, 185),
(741, 'The Last Judgment', 1, 186),
(742, 'The Creation of Adam', 0, 186),
(743, 'The Last Supper', 0, 186),
(744, 'Judgment Day', 0, 186),
(745, 'Maya Lin', 1, 187),
(746, 'Frank Gehry', 0, 187),
(747, 'I.M. Pei', 0, 187),
(748, 'Zaha Hadid', 0, 187),
(749, 'Abstract Expressionism', 1, 188),
(750, 'Dada', 0, 188),
(751, 'Cubism', 0, 188),
(752, 'Fauvism', 0, 188),
(753, 'Raphael', 1, 189),
(754, 'Leonardo da Vinci', 0, 189),
(755, 'Michelangelo', 0, 189),
(756, 'Titian', 0, 189),
(757, 'Salvador Dalí', 1, 190),
(758, 'Pablo Picasso', 0, 190),
(759, 'Frida Kahlo', 0, 190),
(760, 'Edvard Munch', 0, 190);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(191, 'Cooking and Food', 'What is the main ingredient in bouillabaisse?', 10),
(192, 'Cooking and Food', 'From which country does the dish "mole" originate?', 10),
(193, 'Cooking and Food', 'Which grain is used to make traditional Italian risotto?', 10),
(194, 'Cooking and Food', 'What is the key ingredient in a traditional Bearnaise sauce?', 10),
(195, 'Cooking and Food', 'Which fruit is used to make traditional Tarte Tatin?', 10),
(196, 'Cooking and Food', 'What type of cuisine is "ceviche" associated with?', 10),
(197, 'Cooking and Food', 'What cheese is traditionally used in Greek salad?', 10),
(198, 'Cooking and Food', 'Which vegetable is the primary ingredient in baba ganoush?', 10),
(199, 'Cooking and Food', 'What is the main ingredient in the Japanese dish "sashimi"?', 10),
(200, 'Cooking and Food', 'What is traditionally the main ingredient in ratatouille?', 10);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(761, 'Fish', 1, 191),
(762, 'Beef', 0, 191),
(763, 'Chicken', 0, 191),
(764, 'Pork', 0, 191),
(765, 'Mexico', 1, 192),
(766, 'Spain', 0, 192),
(767, 'Italy', 0, 192),
(768, 'Portugal', 0, 192),
(769, 'Arborio rice', 1, 193),
(770, 'Basmati rice', 0, 193),
(771, 'Jasmine rice', 0, 193),
(772, 'Brown rice', 0, 193),
(773, 'Tarragon', 1, 194),
(774, 'Parsley', 0, 194),
(775, 'Cilantro', 0, 194),
(776, 'Basil', 0, 194),
(777, 'Apples', 1, 195),
(778, 'Pears', 0, 195),
(779, 'Cherries', 0, 195),
(780, 'Peaches', 0, 195),
(781, 'Peruvian', 1, 196),
(782, 'Mexican', 0, 196),
(783, 'Brazilian', 0, 196),
(784, 'Chilean', 0, 196),
(785, 'Feta', 1, 197),
(786, 'Mozzarella', 0, 197),
(787, 'Cheddar', 0, 197),
(788, 'Parmesan', 0, 197),
(789, 'Eggplant', 1, 198),
(790, 'Zucchini', 0, 198),
(791, 'Potato', 0, 198),
(792, 'Tomato', 0, 198),
(793, 'Fish', 1, 199),
(794, 'Chicken', 0, 199),
(795, 'Beef', 0, 199),
(796, 'Pork', 0, 199),
(797, 'Tomatoes', 1, 200),
(798, 'Potatoes', 0, 200),
(799, 'Eggplant', 0, 200),
(800, 'Carrots', 0, 200);