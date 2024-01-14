-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2024 at 07:51 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411248`
--

-- --------------------------------------------------------

--
-- Table structure for table `otomotif`
--

CREATE TABLE `otomotif` (
  `merk` varchar(26) NOT NULL,
  `warna` varchar(26) NOT NULL,
  `jumlah_roda` int(26) NOT NULL,
  `kecepatan_maksimum` int(26) NOT NULL,
  `jenis_transmisi` int(26) NOT NULL,
  `jenis_motor` varchar(26) NOT NULL,
  `jumlah_turbo` int(26) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `otomotif`
--

INSERT INTO `otomotif` (`merk`, `warna`, `jumlah_roda`, `kecepatan_maksimum`, `jenis_transmisi`, `jenis_motor`, `jumlah_turbo`) VALUES
('honda', 'merah', 4, 80, 0, '', 0),
('toyota', 'hitam', 4, 200, 0, '', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
