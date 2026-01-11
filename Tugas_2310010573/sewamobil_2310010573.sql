-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2026 at 12:09 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sewamobil_2310010573`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `username`, `password`) VALUES
(1, 'admin123', 'admin123'),
(2, 'sari12345', 'sari12345');

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `id_member` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `alamat` text DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telepon` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`id_member`, `username`, `password`, `nama`, `alamat`, `email`, `telepon`) VALUES
(1, 'andi123', 'pass123', 'Andi Saputra', 'Jl. Mawar No.10', 'andi@mail.com', '08123456789'),
(2, 'budi21', 'budi123', 'Budi Hartono', 'Jl. Melati No.5', 'budi@mail.com', '08231234567'),
(3, 'sita90', 'sita123', 'Sita Wulandari', 'Jl. Kenanga No.3', 'sita@mail.com', '08345678901'),
(4, 'dimas123', 'dimas123', 'Dimas Setiawan', 'Handil', 'dimas@gmail.com', '082112345678');

-- --------------------------------------------------------

--
-- Table structure for table `merek`
--

CREATE TABLE `merek` (
  `id_merek` int(11) NOT NULL,
  `merek` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `merek`
--

INSERT INTO `merek` (`id_merek`, `merek`) VALUES
(1, 'Toyota'),
(2, 'Honda'),
(3, 'Suzuki'),
(4, 'Daihatsu'),
(5, 'Ferrari');

-- --------------------------------------------------------

--
-- Table structure for table `mobil`
--

CREATE TABLE `mobil` (
  `id_mobil` int(11) NOT NULL,
  `tanggal` date NOT NULL,
  `id_merek` int(11) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `tahun` int(11) DEFAULT NULL,
  `harga` decimal(12,2) DEFAULT NULL,
  `lokasi` varchar(100) DEFAULT NULL,
  `warna` varchar(50) DEFAULT NULL,
  `keterangan` text DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mobil`
--

INSERT INTO `mobil` (`id_mobil`, `tanggal`, `id_merek`, `type`, `tahun`, `harga`, `lokasi`, `warna`, `keterangan`, `status`) VALUES
(1, '2025-01-01', 1, 'Avanza', 2021, '350000.00', 'Banjarmasin', 'Hitam', 'Mobil keluarga, irit BBM', 'Tersedia'),
(2, '2025-01-05', 2, 'Brio', 2022, '300000.00', 'Banjarbaru', 'Putih', 'Kondisi sangat baik', 'Tersedia'),
(3, '2025-01-10', 3, 'Ertiga', 2020, '330000.00', 'Martapura', 'Silver', 'Muatan banyak', 'Disewakan'),
(4, '2025-01-12', 4, 'Xenia', 2021, '340000.00', 'Banjarmasin', 'Merah', 'AC dingin, nyaman', 'Tersedia'),
(5, '2000-01-01', 5, 'F1', 2025, '2000000.00', 'Cemara', 'Merah', 'Sport Car', 'Disewakan');

-- --------------------------------------------------------

--
-- Table structure for table `tawar`
--

CREATE TABLE `tawar` (
  `id_pesan` int(11) NOT NULL,
  `id_member` int(11) NOT NULL,
  `id_mobil` int(11) NOT NULL,
  `tawar` decimal(12,2) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `pesan` text DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tawar`
--

INSERT INTO `tawar` (`id_pesan`, `id_member`, `id_mobil`, `tawar`, `tanggal`, `pesan`, `status`) VALUES
(1, 1, 1, '300000.00', '2025-02-01', 'Bisa kurang?', 'Pending'),
(2, 2, 3, '280000.00', '2025-02-02', 'Minat sewa besok', 'Diterima'),
(3, 3, 2, '250000.00', '2025-02-03', 'Harga nego ya', 'Ditolak'),
(4, 4, 3, '200000.00', '2000-01-01', 'Deal', 'Diterima');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id_member`);

--
-- Indexes for table `merek`
--
ALTER TABLE `merek`
  ADD PRIMARY KEY (`id_merek`);

--
-- Indexes for table `mobil`
--
ALTER TABLE `mobil`
  ADD PRIMARY KEY (`id_mobil`),
  ADD KEY `fk_mobil_merk` (`id_merek`);

--
-- Indexes for table `tawar`
--
ALTER TABLE `tawar`
  ADD PRIMARY KEY (`id_pesan`),
  ADD KEY `fk_tawar_member` (`id_member`),
  ADD KEY `fk_tawar_mobil` (`id_mobil`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `id_member` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `merek`
--
ALTER TABLE `merek`
  MODIFY `id_merek` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `mobil`
--
ALTER TABLE `mobil`
  MODIFY `id_mobil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tawar`
--
ALTER TABLE `tawar`
  MODIFY `id_pesan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `mobil`
--
ALTER TABLE `mobil`
  ADD CONSTRAINT `fk_mobil_merk` FOREIGN KEY (`id_merek`) REFERENCES `merek` (`id_merek`) ON UPDATE CASCADE;

--
-- Constraints for table `tawar`
--
ALTER TABLE `tawar`
  ADD CONSTRAINT `fk_tawar_member` FOREIGN KEY (`id_member`) REFERENCES `member` (`id_member`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tawar_mobil` FOREIGN KEY (`id_mobil`) REFERENCES `mobil` (`id_mobil`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
