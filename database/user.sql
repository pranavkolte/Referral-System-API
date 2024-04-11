-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 08, 2024 at 09:54 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tests`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` varchar(256) NOT NULL,
  `name` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `referral_code` varchar(256) DEFAULT 'NA',
  `referral_points` int(32) NOT NULL,
  `referral_id` varchar(235) NOT NULL,
  `time` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`, `referral_code`, `referral_points`, `referral_id`, `time`) VALUES
('0f8ff90a5785292a13140274ccd91433cb09110e', 'Yeteral  Jain', 'jain76@gmail.com', 'EA1BF3463F202C9903F95D0EC9E68F932059039DB5A1F5D8FE790BFF6AA36F45', 'N4-AulFt', 0, 'o7NIQYf-', '2024-04-07 16:08:25.118508'),
('19bfea9c52684ab4f19da05e21bed56c77ddb262', 'Alice Smith', 'alice@example.com', '052755796AA30F74FF3F3C9457D58C8024F978D3D8A4A324DFF4224EAEAF950A', NULL, 0, '6_yqKEQ9', '2024-04-07 16:48:22.511756'),
('1fcb48d5e68576a77cc9e0a7b9eba77d3d426870', 'Manali  Shah', 'manali321@gmail.com', 'EA1BF3463F202C9903F95D0EC9E68F932059039DB5A1F5D8FE790BFF6AA36F45', 'HEWnBSTq', 200, 'skJHRHTU', '2024-04-07 21:43:27.649919'),
('374ffc238179297a74fae2e448eaad416031bebd', 'Kunal nhayta', 'kunal@gmail.com', '$2b$12$pjbNUxliMHUELsbfTovQb./kPhipbkx7NTt9qE1Uk2QPGyvtFD4ei', '2zlo9bhW', 0, '_ju5GQCE', '2024-04-08 06:23:50.377262'),
('5ba91e30bf064e77a27560a0d3b92a87433a2c38', 'Duplicate Email', 'john@example.com', '052755796AA30F74FF3F3C9457D58C8024F978D3D8A4A324DFF4224EAEAF950A', NULL, 0, 'RcRV7xmX', '2024-04-07 16:48:22.511756'),
('6b72dd8428e73a6ba71dc8adf7f728d5ab71e3ac', 'John Doe', 'johnny@gmail.com', '063A4BFE6856F7380FF769FAADB8029915734532BCAEC1E7C87A20F1A050174F', 'ABC123', 0, 'Z0jT_qZE', '2024-04-07 16:45:42.727839'),
('6f9cb68f1fba8af7229e0a56e76cd15b8ba8ebc6', 'John Doe', 'john66ny@gmail.com', '063A4BFE6856F7380FF769FAADB8029915734532BCAEC1E7C87A20F1A050174F', 'ABC123', 0, '7Q759wif', '2024-04-07 16:48:22.511756'),
('8bd729dce0ccf5f99eb6549d8c0e681c384e9304', 'Jay  kelani', 'jauykelani@gmail.com', 'EA1BF3463F202C9903F95D0EC9E68F932059039DB5A1F5D8FE790BFF6AA36F45', 'skJHRHTU', 0, 'rXMuwmNJ', '2024-04-07 16:08:25.118508'),
('8be4039601788027bfb8ed54f6337327946789af', 'Aditya  Shah', 'shah32@gmail.com', 'EA1BF3463F202C9903F95D0EC9E68F932059039DB5A1F5D8FE790BFF6AA36F45', 'HEWnBSTq', 100, 'N4-AulFt', '2024-04-07 16:11:51.043864'),
('b80549fcb065ae80c8ea3a84a76ac1c418fecffd', 'Nitesh  Gaikwad', 'nitesh342@gmail.com', '960A6AAE5CA66D0D75B0D8D5E2EF2F781A4C0B8B8B25D59CA73E558F92DECAAB', NULL, 300, 'HEWnBSTq', '2024-04-08 05:28:49.530747'),
('dbec9153722a5c2cca64b5cef950a1e7f1ff0c4f', 'Jagdish Yeple', 'jaggu@gmail.com', '$2b$12$A1HA.kevH6MQVOoKA3/4he.nKQZT4517DI2YGui75UWAulF.olfDG', 'HEWnBSTq', 0, '6vTnpGAs', '2024-04-08 05:27:23.387385'),
('dc9600db9c3fe696a2ef1592f044d27ccf421208', 'John Doe', 'john@gmail.com', '063A4BFE6856F7380FF769FAADB8029915734532BCAEC1E7C87A20F1A050174F', 'ABC123', 100, '2zlo9bhW', '2024-04-08 06:28:10.005410');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
