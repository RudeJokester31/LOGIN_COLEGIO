-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-02-2023 a las 00:44:58
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
(1, 'jeospino', '123', 'Jesly Paola', 'Ospino Porras', 20, 0, 'ADMINISTRADOR', 1),
(2, 'mjortiz', '123', 'Shelsy Mariani', 'Cruz Yepes', 19, 0, 'ADMINISTRADOR', 2),
(3, 'magonzalo', '123', 'Valery Patricia', 'Aguilar Sierra', 12, 6, 'ESTUDIANTE', 3),
(4, 'bavillanueva', '123', 'Bryan Alfonso', 'VILLANUEVA RIVAS', 20, 0, 'ADMINISTRADOR', 4),
(5, 'elepalza', '123', 'Eduardo Lora', 'Epalza Ospino', 16, 10, 'ESTUDIANTE', 5),
(6, 'jaepalza', '123', 'Jhostn Alexander', 'Epalza Manjarrez', 20, 0, 'ADMINISTRADOR', 6),
(7, 'jomarco', '123', 'Jhonny Hilton', 'Epalza Herrera', 49, 0, 'ADMINISTRADOR', 7),
(8, 'kepalza', '123', 'Kewin Jesus', 'Epalza Manjarrez', 17, 0, 'EGRESADO', 8),
(9, 'wemanjarrez', '123', 'Wendy Johana', 'Manjarrez Novoa', 41, 0, 'ADMINISTRADOR', 9);

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
