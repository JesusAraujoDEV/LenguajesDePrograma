import { Controller, Get, Post, Req, Delete, Param, Put, Body, Patch } from '@nestjs/common';
import { CardService } from './card.service';
import { Card } from './card.entity';
import { Request } from 'express';
import { CardInterface } from './card.interface'; // Importa la interfaz

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

  @Delete(':id')
  async remove(@Param('id') id: number): Promise<void> {
    return await this.cardService.remove(id);
  }

  @Put(':id')
  async update(@Param('id') id: number, @Body() cardData: CardInterface): Promise<Card | null> {
    return await this.cardService.update(id, cardData);
  }
  
  @Patch(':id')
  async partialUpdate(@Param('id') id: number, @Body() cardData: Partial<CardInterface>): Promise<Card | null> {
    return await this.cardService.partialUpdate(id, cardData);
  }
}