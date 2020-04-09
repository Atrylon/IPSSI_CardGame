-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  jeu. 09 avr. 2020 à 16:01
-- Version du serveur :  5.7.26
-- Version de PHP :  7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `ipssi_card_game`
--

-- --------------------------------------------------------

--
-- Structure de la table `card`
--

DROP TABLE IF EXISTS `card`;
CREATE TABLE IF NOT EXISTS `card` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(100) NOT NULL,
  `Ressource_type` char(10) NOT NULL,
  `Cost` int(11) NOT NULL,
  `Effect` char(100) NOT NULL,
  `Value` int(11) NOT NULL,
  `Target` char(100) NOT NULL,
  `Rarity` char(100) NOT NULL,
  `Description` char(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `card`
--

INSERT INTO `card` (`Id`, `Name`, `Ressource_type`, `Cost`, `Effect`, `Value`, `Target`, `Rarity`, `Description`) VALUES
(1, 'Destruction de bouclier', 'PA', 1, 'Shield', -5, 'Enemy', 'Rare', 'Détruit le bouclier adverse avec violence'),
(3, 'Foudre', 'PM', 2, 'Life', -20, 'Enemy', 'Rare', 'Lance un éclair sur votre adversaire et lui inflige des dégats'),
(4, 'Potion de soin', 'PO', 3, 'Life', 5, 'Self', 'Epic', 'Une potion de soin qui régénère un certain nombre de point de vie'),
(5, 'Achat de bouclier', 'PO', 3, 'Shield', 5, 'Self', 'Rare', 'Achat d\'un nouveau bouclier'),
(6, 'Soin', 'PM', 3, 'Life', 5, 'Self', 'Rare', 'Sort de soin pour remonter sa vie'),
(7, 'Poison', 'PO', 2, 'Life', -15, 'Enemy', 'Epic', 'Un poison violent qui détruit les points de vie de l\'ennemi'),
(8, 'Amputation', 'PA', 2, 'Life', -25, 'Enemy', 'Epic', 'Un gros coup'),
(9, 'Décapitation', 'PA', 5, 'Life', -100, 'Enemy', 'Legendary', 'Ca OS quoi'),
(2, 'Torrent de flammes', 'PM', 4, 'Life', -50, 'Enemy', 'Epic', 'Déverse un torrent de flammes sur l\'ennemi'),
(10, 'Entaille', 'PA', 1, 'Life', -5, 'Enemy', 'Rare', 'Inflige une large entaille à l\'ennemi'),
(11, 'Boule de feu', 'PM', 1, 'Life', -5, 'Enemy', 'Rare', 'Envoie une boule de feu'),
(12, 'Eclair de givre', 'PM', 1, 'Life', -5, 'Enemy', 'Rare', 'Gele l\'ennemi');

-- --------------------------------------------------------

--
-- Structure de la table `deck`
--

DROP TABLE IF EXISTS `deck`;
CREATE TABLE IF NOT EXISTS `deck` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` char(100) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `deck_cards`
--

DROP TABLE IF EXISTS `deck_cards`;
CREATE TABLE IF NOT EXISTS `deck_cards` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Id_Deck` int(11) NOT NULL,
  `Id_card` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `player`
--

DROP TABLE IF EXISTS `player`;
CREATE TABLE IF NOT EXISTS `player` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Player_index` int(11) NOT NULL,
  `Name` char(100) NOT NULL,
  `HP` int(11) NOT NULL,
  `Shield` int(11) NOT NULL,
  `Gold_generation` int(11) NOT NULL,
  `Gold_stock` int(11) NOT NULL,
  `Mana_generation` int(11) NOT NULL,
  `Mana_stock` int(11) NOT NULL,
  `Action_generation` int(11) NOT NULL,
  `Action_stock` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `player_hand`
--

DROP TABLE IF EXISTS `player_hand`;
CREATE TABLE IF NOT EXISTS `player_hand` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Id_Player` int(11) NOT NULL,
  `Id_card` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
