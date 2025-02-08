import { Controller, Get, Post, Req, Delete, Param, Put, Body, Patch, Query } from '@nestjs/common';
import { CardService } from './card.service';
import { Card } from './card.entity';
import { Request } from 'express';
import { CardInterface } from './card.interface';

@Controller('cards')
export class CardController {
  constructor(private readonly cardService: CardService) {}

  @Get()
  async findAll(@Query('rarity') rarity?: string): Promise<Card[]> {
    // Si la url tiene el parametro rarity
    if (rarity) {
      return await this.cardService.findByRarity(rarity); // Devuelve las cartas filtradas por rarity
    }
    return await this.cardService.findAll(); // Devuelve todas las cartas si no se proporciona rarity
  }

  @Get(':name')
  async findByName(@Param('name') name: string): Promise<Card | null | string> {
    if (name) {
      return await this.cardService.findOneByName(name); 
    }
    return 'Debe proporcionar un nombre'; 
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

  @Get('fill-database')
  fillDatabase(){
    const url = 'https://api.clashroyale.com/v1/cards';
    const token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjBiNzg5ZmM5LTJhZTYtNDliMS1iZmEyLWI0NGFiOTJkMjdlYiIsImlhdCI6MTczOTA0MDQyNiwic3ViIjoiZGV2ZWxvcGVyLzBiNzZlMWJmLWJmN2YtOTU5Zi0wZjg2LWVmMjYyZmQ2ODY1MCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTAuMTIwLjI0OC4xIl0sInR5cGUiOiJjbGllbnQifV19.XJVxWKTu7VtQWy7rTOtjRJ8pdhzGrl6epKLrDsTK1gXQUr35SkFY-y3jpZWXb8aKJBgFE4HdRPvcNq-DziQ9YQ';

    fetch(url, {
      method: 'GET',
      headers: {
        "Authorization": `Bearer ${token}`,
      }, 
    })
    .then(response => response.json())
    .then(data => {
      for (const card of data.items) {
        const cardData: CardInterface = {
          name: card.name,
          image1: card.iconUrls.medium,
          image2: card.iconUrls.evolutionMedium,
          rarity: card.rarity,
          maxLevel: card.maxLevel,
          elixirCost: card.elixirCost,
        };
        this.cardService.create(cardData);
      }
    })
    .catch(error => console.error('Error:', error));
  }
}