
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Card } from './card.entity'
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

  create(cardObject: CardInterface): Promise <Card> {
    const card = this.cardsRepository.create(cardObject)
    return this.cardsRepository.save(card)
  }

  async remove(id: number): Promise<void> {
    await this.cardsRepository.delete(id);
  }
}
