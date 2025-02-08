import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Card } from './cards/card/card.entity';
import { CardModule } from './cards/card/card.module';
import { ServeStaticModule } from '@nestjs/serve-static';
import * as path from 'path';

@Module({
  imports: [
    ServeStaticModule.forRoot({
      rootPath: path.join(__dirname, '..', 'views'),
    }),
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
