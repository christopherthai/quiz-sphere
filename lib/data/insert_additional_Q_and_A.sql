INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(51, 'World History', 'Which ancient civilization built the pyramids?', 1),
(52, 'World History', 'What event marked the beginning of World War II in Europe?', 1),
(53, 'World History', 'Who was the first female Prime Minister of the United Kingdom?', 1),
(54, 'World History', 'What was the code name for the Allied invasion of Normandy in World War II?', 1),
(55, 'World History', 'Who was the first person to orbit the Earth?', 1);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(56, 'Science Discoveries', 'What is the smallest unit of matter?', 2),
(57, 'Science Discoveries', 'Who proposed the theory of evolution by natural selection?', 2),
(58, 'Science Discoveries', 'What is the formula for Einstein’s theory of mass-energy equivalence?', 2),
(59, 'Science Discoveries', 'Who discovered penicillin?', 2),
(60, 'Science Discoveries', 'What is the name of the largest particle accelerator in the world?', 2);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(61, 'Literature', 'Which author wrote "The Catcher in the Rye"?', 3),
(62, 'Literature', 'What is the famous opening line of "Moby-Dick"?', 3),
(63, 'Literature', 'In which novel would you find the character Holden Caulfield?', 3),
(64, 'Literature', 'Who wrote the play "Romeo and Juliet"?', 3),
(65, 'Literature', 'What is the full title of Charles Dickens novel "Oliver Twist"?', 3);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(66, 'Movies', 'Who directed the movie "Schindlers List"?', 4),
(67, 'Movies', 'Which movie features the character Hannibal Lecter?', 4),
(68, 'Movies', 'Who played the role of Forrest Gump in the movie of the same name?', 4),
(69, 'Movies', 'What is the highest-grossing animated film of all time?', 4),
(70, 'Movies', 'Which movie won the Academy Award for Best Picture in 2020?', 4);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(71, 'Music and Instruments', 'Which composer is known as the "Waltz King"?', 5),
(72, 'Music and Instruments', 'What instrument does Kenny G play?', 5),
(73, 'Music and Instruments', 'Which band released the album "The Dark Side of the Moon"?', 5),
(74, 'Music and Instruments', 'Who sang the hit song "Imagine"?', 5),
(75, 'Music and Instruments', 'What is the highest male singing voice?', 5);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(76, 'Computer Science', 'What programming language was created by Guido van Rossum?', 6),
(77, 'Computer Science', 'What is the most popular operating system for web servers?', 6),
(78, 'Computer Science', 'What does the acronym "SQL" stand for?', 6),
(79, 'Computer Science', 'Who invented the World Wide Web?', 6),
(80, 'Computer Science', 'What is the function of a compiler?', 6);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(81, 'Geography', 'Which desert is the largest in the world?', 7),
(82, 'Geography', 'What is the tallest mountain in Africa?', 7),
(83, 'Geography', 'Which continent is the least populated?', 7),
(84, 'Geography', 'What is the capital of Canada?', 7),
(85, 'Geography', 'Which river runs through Baghdad?', 7);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(86, 'Sports', 'What is the highest possible score in a gymnastics routine?', 8),
(87, 'Sports', 'In what year were the first modern Olympic Games held?', 8),
(88, 'Sports', 'Which country hosted the 2016 Summer Olympics?', 8),
(89, 'Sports', 'Who is the all-time leading goal scorer in FIFA World Cup history?', 8),
(90, 'Sports', 'In what year were women allowed to participate in the modern Olympic Games?', 8);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(91, 'Art and Artists', 'Which artist is famous for painting the "Girl with a Pearl Earring"?', 9),
(92, 'Art and Artists', 'Who designed the iconic glass pyramid at the entrance of the Louvre Museum in Paris?', 9),
(93, 'Art and Artists', 'Which art movement did Salvador Dalí belong to?', 9),
(94, 'Art and Artists', 'What is the name of the famous sculpture depicting the Greek goddess of love and beauty?', 9),
(95, 'Art and Artists', 'Which Italian artist is known for his sculptural masterpiece "David"?', 9);

INSERT INTO Questions (id, Subject, content, quiz_id) VALUES
(96, 'Cooking and Food', 'Which country is the origin of paella?', 10),
(97, 'Cooking and Food', 'What is the primary ingredient in hummus?', 10),
(98, 'Cooking and Food', 'What type of cuisine is kimchi associated with?', 10),
(99, 'Cooking and Food', 'What is the main ingredient in a traditional Caprese salad?', 10),
(100, 'Cooking and Food', 'What is the national dish of Japan?', 10);

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

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(281, 'Johann Strauss II', 1, 71),
(282, 'Ludwig van Beethoven', 0, 71),
(283, 'Wolfgang Amadeus Mozart', 0, 71),
(284, 'Franz Schubert', 0, 71);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(285, 'Saxophone', 1, 72),
(286, 'Violin', 0, 72),
(287, 'Piano', 0, 72),
(288, 'Guitar', 0, 72);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(289, 'Reggae', 1, 73),
(290, 'Jazz', 0, 73),
(291, 'Classical', 0, 73),
(292, 'Hip Hop', 0, 73);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(293, 'Michael Jackson', 1, 74),
(294, 'Elvis Presley', 0, 74),
(295, 'Prince', 0, 74),
(296, 'Madonna', 0, 74);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(297, 'Pianissimo', 1, 75),
(298, 'Forte', 0, 75),
(299, 'Piano', 0, 75),
(300, 'Mezzo', 0, 75);

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

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(341, 'France', 1, 86),
(342, 'Germany', 0, 86),
(343, 'Brazil', 0, 86),
(344, 'Spain', 0, 86);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(345, 'Chickpeas', 1, 87),
(346, 'Eggplant', 0, 87),
(347, 'Lentils', 0, 87),
(348, 'Yogurt', 0, 87);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(349, 'Korean', 1, 88),
(350, 'Japanese', 0, 88),
(351, 'Thai', 0, 88),
(352, 'Vietnamese', 0, 88);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(353, 'Tomato', 1, 89),
(354, 'Mozzarella', 0, 89),
(355, 'Basil', 0, 89),
(356, 'Olive Oil', 0, 89);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(357, 'Sushi', 1, 90),
(358, 'Ramen', 0, 90),
(359, 'Tempura', 0, 90),
(360, 'Sashimi', 0, 90);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(361, 'Golden Retriever', 1, 91),
(362, 'Bulldog', 0, 91),
(363, 'Poodle', 0, 91),
(364, 'German Shepherd', 0, 91);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(365, 'Hercules', 1, 92),
(366, 'Zeus', 0, 92),
(367, 'Poseidon', 0, 92),
(368, 'Achilles', 0, 92);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(369, 'Spear', 1, 93),
(370, 'Sword', 0, 93),
(371, 'Bow and Arrow', 0, 93),
(372, 'Shield', 0, 93);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(373, 'The Sistine Chapel', 1, 94),
(374, 'The Parthenon', 0, 94),
(375, 'The Colosseum', 0, 94),
(376, 'The Louvre', 0, 94);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(377, 'Vanilla', 1, 95),
(378, 'Chocolate', 0, 95),
(379, 'Strawberry', 0, 95),
(380, 'Mint', 0, 95);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(381, 'David Bowie', 1, 96),
(382, 'Elton John', 0, 96),
(383, 'Freddie Mercury', 0, 96),
(384, 'Mick Jagger', 0, 96);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(385, 'Violin', 1, 97),
(386, 'Trumpet', 0, 97),
(387, 'Flute', 0, 97),
(388, 'Drums', 0, 97);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(389, 'Punk', 1, 98),
(390, 'Country', 0, 98),
(391, 'Classical', 0, 98),
(392, 'Blues', 0, 98);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(393, 'Beyoncé', 1, 99),
(394, 'Madonna', 0, 99),
(395, 'Adele', 0, 99),
(396, 'Rihanna', 0, 99);

INSERT INTO Answers (id, content, is_correct, question_id) VALUES
(397, 'Falsetto', 1, 100),
(398, 'Soprano', 0, 100),
(399, 'Tenor', 0, 100),
(400, 'Baritone', 0, 100);