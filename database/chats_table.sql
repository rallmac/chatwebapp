CREATE TABLE chats_table (
	chat_id INT AUTO_INCREMENT PRIMARY KEY,
	user1_id INT NOT NULL,
	user2_id INT NOT NULL,
	last_message_id INT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (user1_id) REFERENCES users_table(user_id),
	FOREIGN KEY (user2_id) REFERENCES users_table(user_id),
	FOREIGN KEY (last_message_id) REFERENCES messages_table(message_id)
);
