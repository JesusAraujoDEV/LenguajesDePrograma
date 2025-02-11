import { Controller, Get, Render, Res } from '@nestjs/common';
import { AppService } from './app.service';
import * as path from 'path';
import * as fs from 'fs/promises';
import { CardService } from './cards/card/card.service'; // Importamos el servicio de las Cards para inyectar todas las Cards al html

@Controller()
export class AppController {
  constructor(
    private readonly appService: AppService,
    private readonly cardService: CardService, // Inyecta el CardService
  ) {}

  @Get()
  @Render('index') // Renderiza la vista
  async getHello() {
    const cards = await this.cardService.findAll(); // Selecciona todas las cards
    return { cards }; // Pasa las cards a la vista
  }
}
