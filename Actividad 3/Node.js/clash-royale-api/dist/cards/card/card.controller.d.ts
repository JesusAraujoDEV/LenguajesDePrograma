import { CardService } from './card.service';
import { Card } from './card.entity';
import { Request } from 'express';
export declare class CardController {
    private readonly cardService;
    constructor(cardService: CardService);
    findAll(): Promise<Card[]>;
    create(request: Request): Promise<Card>;
}
