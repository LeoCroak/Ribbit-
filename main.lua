-- original code found on https://github.com/LeoCroak/Ribbit-
function love.load()
    player = {}
    player.x = 50
    player.y = 50
    player.size = 25
    player.speed = 200  -- Increase speed to move smoothly based on time delta
end

function love.update(dt)
    -- Move player up, down, left, and right based on keyboard input
    if love.keyboard.isDown("w") then
        player.y = player.y - player.speed * dt
    end
    if love.keyboard.isDown("s") then
        player.y = player.y + player.speed * dt
    end
    if love.keyboard.isDown("a") then
        player.x = player.x - player.speed * dt
    end
    if love.keyboard.isDown("d") then
        player.x = player.x + player.speed * dt
    end
end

function love.draw()
    love.graphics.circle("fill", player.x, player.y, player.size)
end
