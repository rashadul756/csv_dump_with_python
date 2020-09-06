--
-- Just uncheck "Enable foreign key checks" option under SQL in phpmyadmin
--



SET FOREIGN_KEY_CHECKS = 0; 

TRUNCATE TABLE `damas_microsite_product_service`;
TRUNCATE TABLE `damas_user_microsite_files`;
TRUNCATE TABLE `damas_user_microsite`;
TRUNCATE TABLE `damas_user_membership_detail`;
TRUNCATE TABLE `damas_user_detail`;
TRUNCATE TABLE `damas_user`;

SET FOREIGN_KEY_CHECKS = 1;

--
-- SET SQL_MODE='ALLOW_INVALID_DATES';
--


--
-- Dumping data for table `damas_user`
--

INSERT INTO `damas_user` (`user_id`, `user_email`, `user_password`, `login_count`) VALUES
(1, 'microartshakeel@gmail.com', '20eabe5d64b0e216796e834f52d61fd0b70332fc', 34);


--
-- Dumping data for table `damas_user_detail`
--

INSERT INTO `damas_user_detail` (`user_detail_id`, `membership_id`, `user_id`, `is_frequent_buyer`, `user_lang`, `user_fullname`, `ar_user_fullname`, `user_phone_no`, `user_country`, `user_city`, `user_type`, `user_status`, `approved_by`, `salesperson_id`, `is_mobile_verified`, `mobile_OTP`, `user_last_login`, `user_created_datetime`, `user_modify_datetime`, `keyword`, `landline`, `website`, `ar_keyword`, `fax`) VALUES
(1, 1, 1, 0, 'en', '', '', '966508294744', 190, '', 't', '1', 0, 0, '1', 278139, '2020-04-16 22:08:57', '2018-08-08 13:42:36', '2018-08-08 15:42:36', NULL, NULL, NULL, NULL, NULL);

--
-- Dumping data for table `damas_user_microsite`
--

INSERT INTO `damas_user_microsite` (`microsite_id`, `user_id`, `microsite_theme`, `microsite_domain_name`, `microsite_website`, `microsite_keywords`, `microsite_company_name`, `ar_microsite_company_name`, `microsite_company_logo`, `microsite_ownership_type`, `microsite_establish_year`, `microsite_total_employe`, `microsite_about_company`, `ar_microsite_about_company`, `microsite_chairman_message`, `microsite_service_offering`, `ar_microsite_service_offering`, `microsite_service_looking`, `ar_microsite_service_looking`, `microsite_mission`, `ar_microsite_mission`, `microsite_vission`, `ar_microsite_vission`, `microsite_director_name`, `microsite_director_message`, `ar_microsite_director_message`, `microsite_director_photo`, `microsite_contact_email`, `microsite_contact_phone`, `microsite_contact_mobile`, `microsite_contact_fax`, `microsite_contact_address`, `ar_microsite_contact_address`, `microsite_contact_map`, `microsite_social_facebook`, `microsite_social_twitter`, `microsite_social_gplus`, `microsite_social_linkedin`, `microsite_created_datetime`, `microsite_modified_datetime`, `microsite_status`) VALUES
(1, 1, 'theme1', 'sakeel', 'http://damasmena.com', 'Web Development::Graphics Design::موقع الكتروني', 'Damas Mena Technical Solutions', 'داماس مينا حلول تقنية', '', 1, '', '0-10', '&amp;lt;p&amp;gt;Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.&amp;lt;/p&amp;gt;\r\n&amp;lt;p&amp;gt;Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.&amp;lt;/p&amp;gt;', '&amp;lt;p&amp;gt;لوريم إيبسوم (Lorem Ipsum) هو ببساطة نص شكلي في صناعة الطباعة والتنضيد. لقد كان لوريم إيبسوم النص القياسي المعياري في هذه الصناعة منذ القرن السادس عشر ، عندما أخذت طابعة غير معروفة مجموعة من الأطباق ودمّعتها لعمل كتاب من نوع العينة. وقد نجا ليس فقط خمسة قرون ، ولكن أيضا قفزة في التنضيد الإلكتروني ، وتبقى في الأساس دون تغيير. تم تعميمها في الستينيات مع إصدار أوراق Letraset التي تحتوي على ممرات Lorem Ipsum ، ومؤخرًا مع برامج النشر المكتبي مثل Aldus PageMaker بما في ذلك إصدارات Lorem Ipsum.&amp;lt;/p&amp;gt;\r\n\r\n&amp;lt;p&amp;gt;لوريم إيبسوم (Lorem Ipsum) هو ببساطة نص شكلي في صناعة الطباعة والتنضيد. لقد كان لوريم إيبسوم النص القياسي المعياري في هذه الصناعة منذ القرن السادس عشر ، عندما أخذت طابعة غير معروفة مجموعة من الأطباق ودمّعتها لعمل كتاب من نوع العينة. وقد نجا ليس فقط خمسة قرون ، ولكن أيضا قفزة في التنضيد الإلكتروني ، وتبقى في الأساس دون تغيير. تم تعميمها في الستينيات مع إصدار أوراق Letraset التي تحتوي على ممرات Lorem Ipsum ، ومؤخرًا مع برامج النشر المكتبي مثل Aldus PageMaker بما في ذلك إصدارات Lorem Ipsum.&amp;lt;/p&amp;gt;\r\n', '', '', '', '', '', '', '', '', '', '', '', '', '', 'info@damasmena.com', '59123456', '00966592321380', '5912345688', 'Kingdom of Saudi Arabia, Riyadh \r\nDabbab Street, Next to Saudi Hollandi Bank H.O', 'المملكة العربية السعودية ، الرياض\r\nشارع دباب ، بجانب البنك السعودي الهولندي هـ', '24.6643313,46.7043542', 'http://facebook.com', 'http://twitter.com', 'http://gplus.com', 'http://linkedin.com', '2018-08-09 05:39:47', '2018-08-09 05:39:47', 1);


--
-- Dumping data for table `damas_user_microsite_files`
--

INSERT INTO `damas_user_microsite_files` (`microsite_file_id`, `microsite_id`, `microsite_file_title`, `ar_microsite_file_title`, `microsite_file_name`, `microsite_file_type`, `microsite_file_location`) VALUES
(1, 1, 'aaa', '', '3d-glass-window-logo-mockup-zoom1-150x1505.jpg', 'i', 'c');


--
-- Dumping data for table `damas_microsite_product_service`
--

INSERT INTO `damas_microsite_product_service` (`id`, `user_id`, `type`, `title`, `ar_title`, `description`, `ar_description`, `image`) VALUES
(1, 1, 'p', 'First Product English Arabic', 'المنتج الأول إنجليزي عربي', 'First Product English Arabic Description ', 'المنتج الأول إنجليزي عربي الوصف', '3d-glass-window-logo-mockup-zoom1-150x15020.jpg');


--
-- Dumping data for table `damas_user_membership_detail`
--

INSERT INTO `damas_user_membership_detail` (`md_id`, `user_id`, `membership_id`, `md_add_products`, `md_send_inquiries`, `md_featured_products`, `md_verified_member`, `md_create_microsite`, `md_add_products_used`, `md_send_inquiries_used`, `md_featured_products_used`, `md_membership_start_date`, `md_membership_upgrade_date`, `md_membership_end_date`) VALUES
(1, 1, 1, 5, 5, 2, 0, 1, 0, 1, 0, '2018-08-08', '2018-08-08', '2019-08-08');
