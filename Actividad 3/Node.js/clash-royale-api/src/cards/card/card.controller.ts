import { Controller, Get, Post, Req } from '@nestjs/common';
import { CardService } from './card.service';
import { Card } from './card.entity';
import { Request } from 'express';

@Controller('cards')
export class CardController {
  constructor(private readonly cardService: CardService) {}
  @Get()
  async findAll(): Promise<Card[]> {
    return await this.cardService.findAll();
  }

  @Post()
  async create(@Req() request: Request): Promise<Card> {
    return await this.cardService.create(request.body);
  }
}