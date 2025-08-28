from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def verify_collision_window(ent: Entity):
        if isinstance(ent, Entity):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision_entity(en01, en02):
        is_collision = False
        if isinstance(en01, Enemy) and isinstance(en02, PlayerShot):
            is_collision = True
        elif isinstance(en01, PlayerShot) and isinstance(en02, Enemy):
            is_collision = True
        elif isinstance(en01, Player) and isinstance(en02, EnemyShot):
            is_collision = True
        elif isinstance(en01, EnemyShot) and isinstance(en02, Player):
            is_collision = True

        if is_collision:
            if (
                    en01.rect.right >= en02.rect.left
                    and en01.rect.left <= en02.rect.right
                    and en01.rect.bottom >= en02.rect.top
                    and en01.rect.top <= en02.rect.bottom
            ):
                en01.health -= en02.damage
                en02.health -= en01.damage


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity01 = entity_list[i]
            EntityMediator.verify_collision_window(entity01)
            for a in range(i+1, len(entity_list)):
                entity02 = entity_list[a]
                EntityMediator.verify_collision_entity(entity01, entity02)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]
