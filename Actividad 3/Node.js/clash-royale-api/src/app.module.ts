import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Card } from './cards/card/card.entity';
import { CardModule } from './cards/card/card.module';

@Module({
  imports: [
    CardModule,
    TypeOrmModule.forRoot({
      type: 'sqlite',
      database: 'clash-royal-db',
      entities: [Card],
      synchronize: true,
    }),
    ],
  controllers: [AppController],  
  providers: [AppService],
})
export class AppModule {}
