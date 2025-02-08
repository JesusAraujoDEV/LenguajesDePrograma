import { Controller, Get, Post, Req, Delete, Param, Put, Body, Patch, Query } from '@nestjs/common';
import { CardService } from './card.service';
import { Card } from './card.entity';
import { Request } from 'express';
import { CardInterface } from './card.interface';

@Controller('cards')
export class CardController {
  constructor(private readonly cardService: CardService) {}

  @Get()
  async findAll(@Query('type') type?: string): Promise<Card[]> {
    // Si la url tiene el parametro type
    if (type) {
      return await this.cardService.findByType(type); // Devuelve las cartas filtradas por type
    }
    return await this.cardService.findAll(); // Devuelve todas las cartas si no se proporciona type
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