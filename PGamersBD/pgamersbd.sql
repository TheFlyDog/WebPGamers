-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-11-2020 a las 04:55:14
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pgamersbd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin_interface_theme`
--

CREATE TABLE `admin_interface_theme` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `title` varchar(50) NOT NULL,
  `title_visible` tinyint(1) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `logo_visible` tinyint(1) NOT NULL,
  `css_header_background_color` varchar(10) NOT NULL,
  `title_color` varchar(10) NOT NULL,
  `css_header_text_color` varchar(10) NOT NULL,
  `css_header_link_color` varchar(10) NOT NULL,
  `css_header_link_hover_color` varchar(10) NOT NULL,
  `css_module_background_color` varchar(10) NOT NULL,
  `css_module_text_color` varchar(10) NOT NULL,
  `css_module_link_color` varchar(10) NOT NULL,
  `css_module_link_hover_color` varchar(10) NOT NULL,
  `css_module_rounded_corners` tinyint(1) NOT NULL,
  `css_generic_link_color` varchar(10) NOT NULL,
  `css_generic_link_hover_color` varchar(10) NOT NULL,
  `css_save_button_background_color` varchar(10) NOT NULL,
  `css_save_button_background_hover_color` varchar(10) NOT NULL,
  `css_save_button_text_color` varchar(10) NOT NULL,
  `css_delete_button_background_color` varchar(10) NOT NULL,
  `css_delete_button_background_hover_color` varchar(10) NOT NULL,
  `css_delete_button_text_color` varchar(10) NOT NULL,
  `css` longtext NOT NULL,
  `list_filter_dropdown` tinyint(1) NOT NULL,
  `related_modal_active` tinyint(1) NOT NULL,
  `related_modal_background_color` varchar(10) NOT NULL,
  `related_modal_rounded_corners` tinyint(1) NOT NULL,
  `logo_color` varchar(10) NOT NULL,
  `recent_actions_visible` tinyint(1) NOT NULL,
  `favicon` varchar(100) NOT NULL,
  `related_modal_background_opacity` varchar(5) NOT NULL,
  `env_name` varchar(50) NOT NULL,
  `env_visible_in_header` tinyint(1) NOT NULL,
  `env_color` varchar(10) NOT NULL,
  `env_visible_in_favicon` tinyint(1) NOT NULL,
  `related_modal_close_button_visible` tinyint(1) NOT NULL,
  `language_chooser_active` tinyint(1) NOT NULL,
  `language_chooser_display` varchar(10) NOT NULL,
  `list_filter_sticky` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `admin_interface_theme`
--

INSERT INTO `admin_interface_theme` (`id`, `name`, `active`, `title`, `title_visible`, `logo`, `logo_visible`, `css_header_background_color`, `title_color`, `css_header_text_color`, `css_header_link_color`, `css_header_link_hover_color`, `css_module_background_color`, `css_module_text_color`, `css_module_link_color`, `css_module_link_hover_color`, `css_module_rounded_corners`, `css_generic_link_color`, `css_generic_link_hover_color`, `css_save_button_background_color`, `css_save_button_background_hover_color`, `css_save_button_text_color`, `css_delete_button_background_color`, `css_delete_button_background_hover_color`, `css_delete_button_text_color`, `css`, `list_filter_dropdown`, `related_modal_active`, `related_modal_background_color`, `related_modal_rounded_corners`, `logo_color`, `recent_actions_visible`, `favicon`, `related_modal_background_opacity`, `env_name`, `env_visible_in_header`, `env_color`, `env_visible_in_favicon`, `related_modal_close_button_visible`, `language_chooser_active`, `language_chooser_display`, `list_filter_sticky`) VALUES
(1, 'Django', 1, 'Django administration', 1, '', 1, '#0C4B33', '#F5DD5D', '#44B78B', '#FFFFFF', '#C9F0DD', '#44B78B', '#FFFFFF', '#FFFFFF', '#C9F0DD', 1, '#0C3C26', '#156641', '#0C4B33', '#0C3C26', '#FFFFFF', '#BA2121', '#A41515', '#FFFFFF', '', 1, 1, '#000000', 1, '#FFFFFF', 1, '', '0.3', '', 1, '#E74C3C', 1, 1, 1, 'code', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add Theme', 1, 'add_theme'),
(2, 'Can change Theme', 1, 'change_theme'),
(3, 'Can delete Theme', 1, 'delete_theme'),
(4, 'Can view Theme', 1, 'view_theme'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add user', 5, 'add_user'),
(18, 'Can change user', 5, 'change_user'),
(19, 'Can delete user', 5, 'delete_user'),
(20, 'Can view user', 5, 'view_user'),
(21, 'Can add content type', 6, 'add_contenttype'),
(22, 'Can change content type', 6, 'change_contenttype'),
(23, 'Can delete content type', 6, 'delete_contenttype'),
(24, 'Can view content type', 6, 'view_contenttype'),
(25, 'Can add session', 7, 'add_session'),
(26, 'Can change session', 7, 'change_session'),
(27, 'Can delete session', 7, 'delete_session'),
(28, 'Can view session', 7, 'view_session'),
(29, 'Can add contacto', 8, 'add_contacto'),
(30, 'Can change contacto', 8, 'change_contacto'),
(31, 'Can delete contacto', 8, 'delete_contacto'),
(32, 'Can view contacto', 8, 'view_contacto'),
(33, 'Can add marca', 9, 'add_marca'),
(34, 'Can change marca', 9, 'change_marca'),
(35, 'Can delete marca', 9, 'delete_marca'),
(36, 'Can view marca', 9, 'view_marca'),
(37, 'Can add producto', 10, 'add_producto'),
(38, 'Can change producto', 10, 'change_producto'),
(39, 'Can delete producto', 10, 'delete_producto'),
(40, 'Can view producto', 10, 'view_producto'),
(41, 'Can add pedido', 11, 'add_pedido'),
(42, 'Can change pedido', 11, 'change_pedido'),
(43, 'Can delete pedido', 11, 'delete_pedido'),
(44, 'Can view pedido', 11, 'view_pedido');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$bvyR6MSn6qpt$FbY4hAhOGYsgccQKZrkx6k+QNjxwjLtjhCt20YaZfdg=', '2020-11-02 03:13:17.984843', 1, 'admin', '', '', 'nicoalexander993@gmail.com', 1, 1, '2020-11-02 01:56:58.712822'),
(2, 'pbkdf2_sha256$216000$kDaTgEWHqhsB$dB6ZjSIrgcnCAGAcAlvy8B/kIJgPjbdfdpZ2PdsGsgg=', '2020-11-02 03:44:25.880832', 0, 'Administrador', 'Nicolas', 'Gfell', 'nicoalexander993@gmail.com', 0, 1, '2020-11-02 02:51:59.000000'),
(3, 'pbkdf2_sha256$216000$v7KL0Sddf23F$KAVtmhxpfjquNM20mlIluvGJ3aGjFCtKLvvLrzZc/b0=', '2020-11-02 03:32:02.868170', 0, 'Cliente', 'Pablo', 'Alarcon', 'PAlarcon@gmail.com', 0, 1, '2020-11-02 02:52:26.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_user_user_permissions`
--

INSERT INTO `auth_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
(1, 2, 33),
(2, 2, 34),
(3, 2, 35),
(4, 2, 36),
(5, 2, 37),
(6, 2, 38),
(7, 2, 39),
(8, 2, 40),
(9, 3, 41),
(10, 3, 42),
(11, 3, 43),
(12, 3, 44);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-11-02 02:06:38.914833', '1', 'p1', 1, '[{\"added\": {}}]', 10, 1),
(2, '2020-11-02 02:53:38.462573', '2', 'Administrador', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 5, 1),
(3, '2020-11-02 02:54:17.200238', '3', 'Cliente', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 5, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'admin', 'logentry'),
(1, 'admin_interface', 'theme'),
(4, 'auth', 'group'),
(3, 'auth', 'permission'),
(5, 'auth', 'user'),
(6, 'contenttypes', 'contenttype'),
(8, 'PGamersApp', 'contacto'),
(9, 'PGamersApp', 'marca'),
(11, 'PGamersApp', 'pedido'),
(10, 'PGamersApp', 'producto'),
(7, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'PGamersApp', '0001_initial', '2020-11-02 01:53:37.711883'),
(2, 'contenttypes', '0001_initial', '2020-11-02 01:53:38.008688'),
(3, 'auth', '0001_initial', '2020-11-02 01:53:38.243075'),
(4, 'admin', '0001_initial', '2020-11-02 01:53:39.044922'),
(5, 'admin', '0002_logentry_remove_auto_add', '2020-11-02 01:53:39.240391'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2020-11-02 01:53:39.259340'),
(7, 'admin_interface', '0001_initial', '2020-11-02 01:53:39.353563'),
(8, 'admin_interface', '0002_add_related_modal', '2020-11-02 01:53:39.507153'),
(9, 'admin_interface', '0003_add_logo_color', '2020-11-02 01:53:39.545051'),
(10, 'admin_interface', '0004_rename_title_color', '2020-11-02 01:53:39.565995'),
(11, 'admin_interface', '0005_add_recent_actions_visible', '2020-11-02 01:53:39.599905'),
(12, 'admin_interface', '0006_bytes_to_str', '2020-11-02 01:53:39.660777'),
(13, 'admin_interface', '0007_add_favicon', '2020-11-02 01:53:39.695683'),
(14, 'admin_interface', '0008_change_related_modal_background_opacity_type', '2020-11-02 01:53:39.758583'),
(15, 'admin_interface', '0009_add_enviroment', '2020-11-02 01:53:39.832643'),
(16, 'admin_interface', '0010_add_localization', '2020-11-02 01:53:39.851543'),
(17, 'admin_interface', '0011_add_environment_options', '2020-11-02 01:53:39.963077'),
(18, 'admin_interface', '0012_update_verbose_names', '2020-11-02 01:53:39.974248'),
(19, 'admin_interface', '0013_add_related_modal_close_button', '2020-11-02 01:53:40.038743'),
(20, 'admin_interface', '0014_name_unique', '2020-11-02 01:53:40.075834'),
(21, 'admin_interface', '0015_add_language_chooser_active', '2020-11-02 01:53:40.115683'),
(22, 'admin_interface', '0016_add_language_chooser_display', '2020-11-02 01:53:40.155980'),
(23, 'admin_interface', '0017_change_list_filter_dropdown', '2020-11-02 01:53:40.164956'),
(24, 'admin_interface', '0018_theme_list_filter_sticky', '2020-11-02 01:53:40.206711'),
(25, 'contenttypes', '0002_remove_content_type_name', '2020-11-02 01:53:40.332810'),
(26, 'auth', '0002_alter_permission_name_max_length', '2020-11-02 01:53:40.427607'),
(27, 'auth', '0003_alter_user_email_max_length', '2020-11-02 01:53:40.456567'),
(28, 'auth', '0004_alter_user_username_opts', '2020-11-02 01:53:40.469533'),
(29, 'auth', '0005_alter_user_last_login_null', '2020-11-02 01:53:40.552143'),
(30, 'auth', '0006_require_contenttypes_0002', '2020-11-02 01:53:40.557093'),
(31, 'auth', '0007_alter_validators_add_error_messages', '2020-11-02 01:53:40.571055'),
(32, 'auth', '0008_alter_user_username_max_length', '2020-11-02 01:53:40.603024'),
(33, 'auth', '0009_alter_user_last_name_max_length', '2020-11-02 01:53:40.629935'),
(34, 'auth', '0010_alter_group_name_max_length', '2020-11-02 01:53:40.658987'),
(35, 'auth', '0011_update_proxy_permissions', '2020-11-02 01:53:40.675976'),
(36, 'auth', '0012_alter_user_first_name_max_length', '2020-11-02 01:53:40.705643'),
(37, 'sessions', '0001_initial', '2020-11-02 01:53:40.748053');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pgamersapp_contacto`
--

CREATE TABLE `pgamersapp_contacto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `tipo_consulta` int(11) NOT NULL,
  `mensaje` longtext NOT NULL,
  `avisos` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pgamersapp_contacto`
--

INSERT INTO `pgamersapp_contacto` (`id`, `nombre`, `correo`, `tipo_consulta`, `mensaje`, `avisos`) VALUES
(1, 'Nicolas', 'nicoalexander993@gmail.com', 1, 'blablabla', 1),
(2, 'Nicolas', 'nicoalexander993@gmail.com', 1, 'blablabla', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pgamersapp_marca`
--

CREATE TABLE `pgamersapp_marca` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pgamersapp_marca`
--

INSERT INTO `pgamersapp_marca` (`id`, `nombre`) VALUES
(1, 'Komc'),
(4, 'Hyperx'),
(5, 'JBL'),
(6, 'maxell'),
(7, 'Trust');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pgamersapp_pedido`
--

CREATE TABLE `pgamersapp_pedido` (
  `id` int(11) NOT NULL,
  `rut` varchar(12) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `a_paterno` varchar(50) NOT NULL,
  `a_materno` varchar(50) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pgamersapp_producto`
--

CREATE TABLE `pgamersapp_producto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `precio` int(11) NOT NULL,
  `descripcion` longtext NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `marca_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pgamersapp_producto`
--

INSERT INTO `pgamersapp_producto` (`id`, `nombre`, `precio`, `descripcion`, `imagen`, `marca_id`) VALUES
(6, 'Audifonos Gamer Komc', 20000, 'Diseño minimalista moderno y ergonómico en 2 versiones que no dejará indiferente a los gustos más exigentes cómodos y proporcionan un ajuste perfecto en la cabeza presionando los altavoces contra los oídos y aislando.', 'productos/audifono_1_jMaLwyl.jpg', 1),
(7, 'Audifonos Gamer Hyperx', 60000, 'Auriculares ligeros con almohadillas que giran 90 grados Controladores direccionales de 50 mm para ofrecer una mayor precisión del sonido Espuma viscoelástica exclusiva de HyperX Control deslizante de acero ajustable Control de volumen intuitivo situado en el casco Micrófono con cancelación de sonido y silenciado con un movimiento del brazo del micrófono Compatibilidad multiplataforma Audifonos gamer HyperX Cloud Stinger Negro.', 'productos/Audifono_2_jpliLC5.jpg', 4),
(8, 'Audífono T 500', 30000, 'Sus materiales ligeros, suaves almohadillas y banda de sujeción acolchada te permitirán llevar estos auriculares cómodamente durante largos periodos de tiempo. El diseño plegable hace que llevar estos auriculares sea muy fácil, permitiéndote disfrutar de tu música favorita dónde y cuándo quieras.', 'productos/audifono_3_yZyMhfe.jpg', 5),
(9, 'Maxell Teclado Gamer Iluminado Kb', 25000, 'Teclado CA/KB, Iluminación RGB, Teclas anti-fantasma, Set de teclas adicionales', 'productos/teclado_1.jpg', 6),
(10, 'Teclado Con Touchpad Theza Wireless', 46990, 'Teclado Gris Oscuro', 'productos/teclado_2.jpg', 7),
(11, 'Teclado Mecánico Gaming Usb Iluminado', 100000, 'Interruptores de respuesta rápida GXT de color blanco con una resistencia de hasta 50 millones de pulsaciones. Retroiluminación LED integral con retroiluminación por tecla mejorada. Tecnología N-Key Rollover para desactivar el efecto fantasma. Tasa de sondeo de 1.000 Hz y tiempo de respuesta de 5 ms. Con memoria integrada para programar 4 teclas de macro.', 'productos/teclado_3.jpg', 7);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `admin_interface_theme`
--
ALTER TABLE `admin_interface_theme`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_interface_theme_name_30bda70f_uniq` (`name`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `pgamersapp_contacto`
--
ALTER TABLE `pgamersapp_contacto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pgamersapp_marca`
--
ALTER TABLE `pgamersapp_marca`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pgamersapp_pedido`
--
ALTER TABLE `pgamersapp_pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `PGamersApp_pedido_producto_id_cfb656df_fk_PGamersApp_producto_id` (`producto_id`);

--
-- Indices de la tabla `pgamersapp_producto`
--
ALTER TABLE `pgamersapp_producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `PGamersApp_producto_marca_id_dce0cdb5_fk_PGamersApp_marca_id` (`marca_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `admin_interface_theme`
--
ALTER TABLE `admin_interface_theme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `pgamersapp_contacto`
--
ALTER TABLE `pgamersapp_contacto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `pgamersapp_marca`
--
ALTER TABLE `pgamersapp_marca`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `pgamersapp_pedido`
--
ALTER TABLE `pgamersapp_pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `pgamersapp_producto`
--
ALTER TABLE `pgamersapp_producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `pgamersapp_pedido`
--
ALTER TABLE `pgamersapp_pedido`
  ADD CONSTRAINT `PGamersApp_pedido_producto_id_cfb656df_fk_PGamersApp_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `pgamersapp_producto` (`id`);

--
-- Filtros para la tabla `pgamersapp_producto`
--
ALTER TABLE `pgamersapp_producto`
  ADD CONSTRAINT `PGamersApp_producto_marca_id_dce0cdb5_fk_PGamersApp_marca_id` FOREIGN KEY (`marca_id`) REFERENCES `pgamersapp_marca` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
