using hahaRU.Lib;
using hahaRU.Models;
using hahaRU.Storage;
using hahaRU.Storage.Entity;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using System.Threading.Tasks;

namespace hahaRU.Managers
{
    public class ApiManager: IApiManager
    {
        private Context _context;

        public ApiManager(Context context)
        {
            _context = context;
        }

        public object changeContentDisLiked(int postId, object type, HttpContext httpContext)
        {
            int? id = httpContext.Session.GetInt32("id");
            if (id == null) return new JsonStatus() { status = "error", text = "вы не зарегестрированы" };
            DbSet<Mem> db;
            IContent post;
            switch (type)
            {
                case "mem":
                    post = _context.Mems.Where(post => post.Id == postId).First();
                    break;
                case "funnyWord":
                    post = _context.FunnyWords.Where(post => post.Id == postId).First();
                    break;
                case "video":
                    post = _context.Videos.Where(post => post.Id == postId).First();
                    break;
                default:
                    post = _context.Anecdots.Where(post => post.Id == postId).First();
                    break;
            }
            if (post == null) return new JsonStatus() { status = "error", text = "post не существует" };
            IdList likes = new IdList(post.Dislikes);
            if (likes.hasId((int)id))
            {
                likes.removeId((int)id);
                post.Dislikes = likes.toString();
                post.DislikesCount--;
            }
            else
            {
                likes.AddId((int)id);
                post.Dislikes = likes.toString();
                post.DislikesCount++;
            }
            _context.SaveChanges();
            return new JsonStatus()
            {
                status = "ok",
                text = "все окей",
                value = new ContentData()
                {
                    IsDisLiked = likes.hasId((int)id) ? 1 : 0,
                    DislikesCount = post.DislikesCount,
                    Id = post.Id
                }
            };
        }

        public object changeContentLiked(int postId, string type, HttpContext httpContext)
        {
            int? id = httpContext.Session.GetInt32("id");
            if (id == null) return new JsonStatus() { status = "error", text = "вы не зарегестрированы" };
            IContent post;
            switch (type)
            {
                case "mem":
                    post = _context.Mems.Where(post => post.Id == postId).First();
                    break;
                case "funnyWord":
                    post = _context.FunnyWords.Where(post => post.Id == postId).First();
                    break;
                case "video":
                    post = _context.Videos.Where(post => post.Id == postId).First();
                    break;
                default:
                    post = _context.Anecdots.Where(post => post.Id == postId).First();
                    break;
            }
            if (post == null) return new JsonStatus() { status = "error", text = "post не существует" };
            IdList likes = new IdList(post.Likes);
            if (likes.hasId((int)id))
            {
                likes.removeId((int)id);
                post.Likes = likes.toString();
                post.LikesCount--;
            }
            else
            {
                likes.AddId((int)id);
                post.Likes = likes.toString();
                post.LikesCount++;
            }
            _context.SaveChanges();
            return new JsonStatus()
            {
                status = "ok",
                text = "все окей",
                value = new ContentData()
                {
                    IsLiked = likes.hasId((int)id) ? 1 : 0,
                    LikesCount = post.LikesCount,
                    Id = post.Id
                }
            };
        }

        public object changeDisLiked(int postId, HttpContext httpContext)
        {
            int? id = httpContext.Session.GetInt32("id");
            if (id == null) return new JsonStatus() { status = "error", text = "вы не зарегестрированы" };
            List<Post> posts = _context.Posts.Where(post => post.Id == postId).ToList();
            if (posts.Count == 0) return new JsonStatus() { status = "error", text = "post не существует" };
            Post post = posts[0];
            IdList likes = new IdList(post.Dislikes);
            if (likes.hasId((int)id))
            {
                likes.removeId((int)id);
                post.Dislikes = likes.toString();
                post.DislikesCount--;
            }
            else
            {
                likes.AddId((int)id);
                post.Dislikes = likes.toString();
                post.DislikesCount++;
            }
            _context.SaveChanges();
            return new JsonStatus() { status = "ok", 
                text = "все окей",
                value = new PostData()
                {
                    IsDisLiked = likes.hasId((int)id) ? 1 : 0,
                    DislikesCount = post.DislikesCount,
                    Id = post.Id
                }
            };
        }

        public object changeLiked(int postId, HttpContext httpContext)
        {
            int? id = httpContext.Session.GetInt32("id");
            if (id == null) return new JsonStatus() { status = "error", text = "вы не зарегестрированы" };
            List<Post> posts = _context.Posts.Where(post => post.Id == postId).ToList();
            if(posts.Count==0) return new JsonStatus() { status = "error", text = "post не существует" };
            Post post = posts[0];
            IdList likes = new IdList(post.Likes);
            if(likes.hasId((int)id))
            {
                likes.removeId((int)id);
                post.Likes = likes.toString();
                post.LikesCount--;
            }
            else
            {
                likes.AddId((int)id);
                post.Likes = likes.toString();
                post.LikesCount++;
            }
            _context.SaveChanges();
            return new JsonStatus() { 
                status = "ok", 
                text = "все окей", 
                value = new PostData() {
                    IsLiked= likes.hasId((int)id)?1:0,
                    LikesCount= post.LikesCount,
                    Id=post.Id
                } 
            };
        }

        public object getContents(getPostReq data, HttpContext httpContext)
        {
            int count = data.Count ?? 20;
            int offset = data.Offset ?? 0;
            int? id = httpContext.Session.GetInt32("id");
            id = (id == null) ? 0 : id;
            List<IContent> posts;
            switch (data.type)
            {
                case "mem":
                    posts = _context.Mems.OrderByDescending(x => x.LikesCount).Skip(offset).Take(count).ToList().Cast<IContent>().ToList();
                    break;
                case "funnyWord":
                    posts = _context.FunnyWords.OrderByDescending(x => x.LikesCount).Skip(offset).Take(count).ToList().Cast<IContent>().ToList();
                    break;
                case "video":
                    posts = _context.Videos.OrderByDescending(x => x.LikesCount).Skip(offset).Take(count).ToList().Cast<IContent>().ToList();
                    break;
                default:
                    posts = _context.Anecdots.OrderByDescending(x => x.LikesCount).Skip(offset).Take(count).ToList().Cast<IContent>().ToList();
                    break;
            }
            List<ContentData> Contents = new List<ContentData>();
            foreach (IContent post in posts)
            {
                Contents.Add(new ContentData()
                {
                    Id = post.Id,
                    Text = post.Text,
                    Date = post.Date,
                    ImgSrc = post.ImgSrc,
                    VideoSrc=post.VideoSrc,
                    IsLiked = (new IdList(post.Likes)).hasId((int)id) ? 1 : 0,
                    IsDisLiked = (new IdList(post.Dislikes)).hasId((int)id) ? 1 : 0,
                    LikesCount = post.LikesCount,
                    DislikesCount = post.DislikesCount
                });
            }
            return Contents;
        }

        public object getPosts(getPostReq data, HttpContext httpContext)
        {
            int count= data.Count ?? 20;
            int offset = data.Offset ?? 0;
            int? id = httpContext.Session.GetInt32("id");
            id = (id==null)?0:id;
            List<Post> posts;
            if (data.UserId == null)
                posts= _context.Posts.OrderByDescending(x => x.LikesCount).Skip(offset).Take(count).ToList();
            else
                posts = _context.Posts.Where(e => e.UserId == data.UserId).OrderByDescending(x => x.Id).Skip(offset).Take(count).ToList();

            List<PostData> Posts = new List<PostData>();
            foreach(Post post in posts)
            {
                Posts.Add(new PostData()
                {
                    Id = post.Id,
                    Text = post.Text,
                    Date = post.Date,
                    UserId = post.UserId,
                    ImgSrc = post.ImgSrc,
                    IsLiked = (new IdList(post.Likes)).hasId((int)id) ? 1: 0,
                    IsDisLiked = (new IdList(post.Dislikes)).hasId((int)id) ? 1 : 0,
                    LikesCount=post.LikesCount,
                    DislikesCount=post.DislikesCount
                });
            }
            return Posts;
        }

        public object getRundomAnecdot()
        {
            return new object();
        }

        public object getRundomMemImg()
        {
            int count = _context.memPictures.Count();
            if (count == 0) return new JsonStatus() { status = "error", text = "нет изображений" };
            Random rnd = new Random();
            int id = rnd.Next(1, count+1);
            memPictures mem = _context.memPictures.Where(mem => mem.Id == id).First();
            return new JsonStatus() { status = "ok", value = mem };
        }

        public object getRundomMemText()
        {
            int count = _context.memTexts.Count();
            if (count == 0) return new JsonStatus() { status = "error", text = "нет текстов" };
            Random rnd = new Random();
            int id = rnd.Next(1, count+1);
            memText mem = _context.memTexts.Where(mem => mem.Id == id).First();
            return new JsonStatus() { status = "ok", value=mem };
        }

        public object getRundomVideo()
        {
            int count = _context.VideoSrcs.Count();
            if (count == 0) return new JsonStatus() { status = "error", text = "нет видео" };
            Random rnd = new Random();
            int id = rnd.Next(1, count);
            VideoSrc video = _context.VideoSrcs.Where(mem => mem.Id == id).First();
            return new JsonStatus() { status = "ok", value = video };
        }

        public string getUser(int id)
        {
            var users = _context.Users.Where(e => e.Id == id).ToList();
            if (users.Count == 0) return "{}";
            users[0].Password = null;
            return JsonSerializer.Serialize(users[0]);
        }

        public string getUser(HttpContext httpContext)
        {
            int? id = httpContext.Session.GetInt32("id");
            if (id == null) return "{}";
            var users = _context.Users.Where(e => e.Id == id).ToList();
            if (users.Count == 0) return "{}";
            users[0].Password = null;
            return JsonSerializer.Serialize(users[0]);
        }

        public object getVideos(getPostReq data, HttpContext httpContext)
        {
            throw new NotImplementedException();
        }
        public object saveAva(IFormFileCollection files, string webRootPath, HttpContext httpContext)
        {
            int? id = httpContext.Session.GetInt32("id");
            if (id == null) return new JsonStatus() { status = "error", text = "Вы не авторизовались" };
            string path = "";
            if(files.Count==0) return new JsonStatus() { status = "error", text = "Картинка не найдена" };
            var file = files[0];
            path = "/img/avaImgs/" + file.FileName;
                using (var fileStream = new FileStream(webRootPath + path, FileMode.Create))
                {
                    file.CopyTo(fileStream);
                }
                memPictures pic = new memPictures() { ImgSrc = file.FileName };
            User user = _context.Users.Single(user => user.Id == (int)id);
            if(user==null) return new JsonStatus() { status = "error", text = "Вы не авторизовались 2" };
            user.AvatarSrc = path;
            _context.SaveChanges();
            return new JsonStatus() { status = "ok", value = path };
        }

        public object saveMem(IFormFileCollection files, string webRootPath)
        {
            foreach (var file in files)
            {
                string path = "/img/memGenerated/" + file.FileName;
                using (var fileStream = new FileStream(webRootPath + path, FileMode.Create))
                {
                    file.CopyTo(fileStream);
                }
                Mem mem = new Mem() { ImgSrc = path };
                _context.Mems.Add(mem);
            }
            _context.SaveChanges();
            return new object();
        }

        public object saveMem(string imgBase64, string webRootPath)
        {
            int count = _context.Mems.Count();
            string path = $"/img/memGenerated/img{count}.png";
            File.WriteAllBytes(webRootPath + path, Convert.FromBase64String(imgBase64));
            Mem mem = new Mem() { ImgSrc = path };
            _context.Mems.Add(mem);
            _context.SaveChanges();
            return new JsonStatus() { status = "ok",value=mem };
        }

        public object saveMemPic(IFormFileCollection files, string webRootPath)
        {
            string path="";
            foreach (var file in files)
            {
                path = "/img/memImgs/" + file.FileName;
                using (var fileStream = new FileStream(webRootPath + path, FileMode.Create))
                {
                    file.CopyTo(fileStream);
                }
                memPictures pic = new memPictures() { ImgSrc = file.FileName };
                _context.memPictures.Add(pic);
                _context.SaveChanges();
            }
           return new JsonStatus() { status = "ok", value = path };
        }
            
        

        public object sendPost(Post post, HttpContext httpContext)
        {
            int? id = httpContext.Session.GetInt32("id");
            if (id == null) return new JsonStatus() { status = "error", text = "Вы не авторизовались" };
            if (post.Text == "") return new JsonStatus() { status = "error", text = "Пост не может быть без текста" };
            if (post.Text == null) return new JsonStatus() { status = "error", text = "текст не найден" };
            Post post1 = new Post()
            {
                Text = post.Text,
                UserId = (int)id,
                Date = post.Date
            };
            _context.Posts.Add(post1);
            _context.SaveChanges();
            return new JsonStatus() { status="ok",text="ok"};
        }

        public string updateUser(User user, HttpContext httpContext)
        {
            if (user.Id==0) return "Id is not find";
            int? id = httpContext.Session.GetInt32("id");
            if(id==null) return "Your doesn't auth";
            if(id!=user.Id) return "нельзя изменять чужой аккаунт";
            User userNew = _context.Users
                .Where(c => c.Id == id)
                .First();
            if (userNew == null) return "how";
            if (user.AvatarSrc != null) userNew.AvatarSrc = user.AvatarSrc;
            if (user.Date != null) userNew.Date = user.Date;
            if (user.Status != null) userNew.Status = user.Status;
            if (user.FavoriteJoke != null) userNew.FavoriteJoke = user.FavoriteJoke;
            if (user.VkLink != null) userNew.VkLink = user.VkLink;
            if (user.Telegram != null) userNew.Telegram = user.Telegram;
            if (user.InstaLink != null) userNew.InstaLink = user.InstaLink;
            _context.SaveChanges();
            return "ok";
        }

        
    }
}
