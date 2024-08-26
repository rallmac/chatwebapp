CREATE TABLE messages_table (
	message_id INT AUTO_INCREMENT PRIMARY KEY,
	sender_id INT NOT NULL,
	receiver_id INT NOT NULL,
	message_content TEXT NOT NULL,
	read_status BOOLEAN DEFAULT FALSE,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (sender_id) REFERENCES users_table(user_id),
	FOREIGN KEY (receiver_id) REFERENCES users_table(user_id),
	INDEX (sender_id),
	INDEX (receiver_id)
);
