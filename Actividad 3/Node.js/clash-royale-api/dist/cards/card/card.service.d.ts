import { Repository } from 'typeorm';
import { Card } from './card.entity';
import { CardInterface } from './card.interface';
export declare class CardService {
    private cardsRepository;
    constructor(cardsRepository: Repository<Card>);
    findAll(): Promise<Card[]>;
    findOne(id: number): Promise<Card | null>;
    create(cardObject: CardInterface): Promise<Card>;
    remove(id: number): Promise<void>;
}
