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