-- Migration idempotente: impose l’unicité (date_reservation, id_creneaux)
-- sur reservations pour empêcher 2 réservations du même créneau pour la même date.

SET @db := DATABASE();

-- Ajouter l’unicité (date_reservation, id_creneaux) si elle n’existe pas.
-- (Le dump actuel montre déjà cet index, mais on le garantit quand même.)

SELECT COUNT(*) INTO @idx_exists
FROM information_schema.statistics
WHERE table_schema = @db
  AND table_name = 'reservations'
  AND index_name = 'uniq_reservation_date_creneaux';

SET @sql := IF(
  @idx_exists = 0,
  'ALTER TABLE reservations ADD UNIQUE KEY uniq_reservation_date_creneaux (date_reservation, id_creneaux)',
  'SELECT 1'
);

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

