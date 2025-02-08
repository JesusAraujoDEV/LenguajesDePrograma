
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Card {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column({ nullable: true })
  image1: string;

  @Column({ nullable: true })
  image2: string;

  @Column({ nullable: true })
  rarity: string;

  @Column({ nullable: true })
  maxLevel: number;
  
  @Column({ nullable: true })
  elixirCost: number;
}
