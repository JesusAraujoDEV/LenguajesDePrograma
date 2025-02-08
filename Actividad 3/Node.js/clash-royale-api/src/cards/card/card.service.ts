import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Card } from './card.entity';
import { CardInterface } from './card.interface';

@Injectable()
export class CardService {
  constructor(
    @InjectRepository(Card)
    private cardsRepository: Repository<Card>,
  ) {}

  findAll(): Promise<Card[]> {
    return this.cardsRepository.find();
  }

  findOne(id: number): Promise<Card | null> {
    return this.cardsRepository.findOneBy({ id });
  }

  findOneByName(name: string): Promise<Card | null> {
    return this.cardsRepository.findOneBy({ name });
  }

  create(cardObject: CardInterface): Promise<Card> {
    const card = this.cardsRepository.create(cardObject);
    return this.cardsRepository.save(card);
  }

  async remove(id: number): Promise<void> {
    await this.cardsRepository.delete(id);
  }

  async update(id: number, cardData: CardInterface): Promise<Card | null> {
    await this.cardsRepository.update(id, cardData);
    return this.cardsRepository.findOneBy({ id });
  }

  async partialUpdate(id: number, cardData: Partial<CardInterface>): Promise<Card | null> {
    await this.cardsRepository.update(id, cardData);
    return this.cardsRepository.findOneBy({ id });
  }

  // Metodo para filtras las cartas por atributo type
  async findByRarity(rarity: string): Promise<Card[]> {
    return this.cardsRepository.find({ where: { rarity } });
  }
}