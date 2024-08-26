CREATE TABLE contacts_table (
	user_id INT NOT NULL,
	contact_user_id INT NOT NULL,
	status ENUM('pending', 'accepted') NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (user_id, contact_user_id),
	FOREIGN KEY (user_id) REFERENCES users_table(user_id),
	FOREIGN KEY (contact_user_id) REFERENCES users_table(user_id)
);
