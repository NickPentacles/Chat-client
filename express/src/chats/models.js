export class Message {
  constructor(uuid, role, content, chat_uuid) {
    this.uuid = uuid;
    this.role = role;
    this.content = content;
    this.chat_uuid = chat_uuid;
  }
}

export class Chat {
  constructor(uuid, name, model, model_ident, project_uuid) {
    this.uuid = uuid; // str
    this.name = name; // str
    this.model = model; // model
    this.model_ident = model_ident; // str
    this.project_uuid = project_uuid; // str
    this.history = {}; // {uuid: Message}
  }

  changeModel = (model, model_ident) => {
    this.model = model;
    this.model_ident = model_ident;
  };

  stream = (messages) => {
    return this.model.respond(messages);
  };

  // addMessage = async () => {
  //   OrmAdd
  //   RedisAdd
  // }

  // getHistory = async () => {
  //   RedisGet or OrmGet
  // }
}
