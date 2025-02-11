import { Controller, Get, Render, Res } from '@nestjs/common';
import { AppService } from './app.service';
import * as path from 'path';
import * as fs from 'fs/promises';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

}
