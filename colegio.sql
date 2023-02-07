-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-02-2023 a las 04:27:46
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `colegio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(10) NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` char(102) DEFAULT NULL,
  `NOMBRES` varchar(30) DEFAULT NULL,
  `APELLIDOS` varchar(30) DEFAULT NULL,
  `EDAD` int(2) DEFAULT NULL,
  `GRADO` int(2) DEFAULT NULL,
  `ROL` varchar(30) DEFAULT NULL,
  `ID_HUELLA` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `username`, `password`, `NOMBRES`, `APELLIDOS`, `EDAD`, `GRADO`, `ROL`, `ID_HUELLA`) VALUES
(1, 'jeospino', 'pbkdf2:sha256:260000$JnRokLgK3plT4UOo$8cedfc0f8928beca555c166aaac0d2a96dc140292694c0c951427a0803e4aa61', 'Jesly Paola', 'Ospino Porras', 20, 0, 'ADMINISTRADOR', 1),
(2, 'mjortiz', 'pbkdf2:sha256:260000$uQr6YyGIiZNGs5vR$e26108f3803f53d3a53c0b9835eef8e7578d9fdb95bcd25f5d2542b8e6370f21', 'MIGUEL JOSE', 'ORTIZ ORTIZ', 13, 6, 'ESTUDIANTE', 2),
(3, 'magonzalo', 'pbkdf2:sha256:260000$v4dNMUn6woRedD4O$7900a613f6aba1c86264095b9639ab7042c337c37d67acd27a262f7f6a43b047', 'marco', 'GONZALO', 15, 9, 'ESTUDIANTE', 3),
(4, 'bavillanueva', 'pbkdf2:sha256:260000$iKn0lEwJUtB2Z0pw$b1df6882fdc7f4ea8242c6ad0fd12862b94c8143fe50fd4a4d5e54c1c8670f77', 'Bryan Alfonso', 'VILLANUEVA RIVAS', 18, 11, 'ESTUDIANTE', 4),
(5, 'elepalza', 'pbkdf2:sha256:260000$AbFKtvMlZ1u6cUdc$c8da4baadcdc3ec86a70e5706d7d7667afd060f0d11ffeff165f1ead8e733dcc', 'EDUARDO LORA', 'EPALZA OSPINO', 16, 10, 'ESTUDIANTE', 5),
(6, 'jaepalza', '123', 'JHOSTIN ALEXANDER', 'EPALZA MANJARREZ', 20, 0, 'ADMINISTRADOR', 6),
(7, 'jomarco', NULL, 'JOSE JOSE', 'MARCO FABIAN', 20, 10, 'ESTUDIANTE', 7),
(8, 'kepalza', NULL, 'KEWIN JESUS', 'EPALZA MANJARREZ', 17, 0, 'EGRESADO', 8),
(9, 'wemanjarrez', NULL, 'WENDY JOHANA', 'MANJARREZ NOVOA', 41, 0, 'ACUDIENTE', 9);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
