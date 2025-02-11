import { Module } from '@nestjs/common';
import { CardController } from './card.controller';
import { Card } from './card.entity';
import { CardService } from './card.service';
import { TypeOrmModule } from '@nestjs/typeorm';

@Module({
  imports: [TypeOrmModule.forFeature([Card])],
  controllers: [CardController],
  providers: [CardService]
})
export class CardModule {}
