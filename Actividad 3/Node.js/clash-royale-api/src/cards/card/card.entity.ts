
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Card {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column({ nullable: true })
  image: string;

  @Column({ nullable: true })
  rarity: string;

  @Column({ nullable: true })
  type: string;

  @Column({ nullable: true })
  damage: number;

  @Column({ nullable: true })
  health: number;

  @Column({ nullable: true })
  targets: string;

  @Column({ nullable: true })
  speed: string;

  @Column({ nullable: true })
  range: string;
}
